package br.com.fiap.votacao;

import br.com.fiap.votacao.model.Pessoa;
import br.com.fiap.votacao.model.Voto;
import br.com.fiap.votacao.service.Apuracao;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Scanner;

public class Aplicacao {

    public static int menu() {
        System.out.println("1 Voto: ");
        System.out.println("2 Resultado: ");
        System.out.println("3 Sair: ");
        Scanner scan = new Scanner(System.in);
        int opcao = scan.nextInt();
        return opcao;
    }

    public static void main(String[] args) {
        Apuracao apuracao = new Apuracao();
        Pessoa c1 = new Pessoa();
        c1.setId(1);
        c1.setNome("Paulo Maluf");
        apuracao.addCandidato(c1);

        Pessoa c2 = new Pessoa();
        c2.setId(2);
        c2.setNome("Mario Covas");
        apuracao.addCandidato(c2);

        Pessoa c3 = new Pessoa();
        c3.setId(3);
        c3.setNome("Franco Montoro");
        apuracao.addCandidato(c3);

        int opcao = 0;
        while (opcao != 3) {
            opcao = menu();
            if (opcao == 1) {
                Voto v = votando(apuracao.getCandidatos());
                apuracao.addVoto(v);
            }
            else if (opcao == 2) {
                Pessoa vencedor = apuracao.vencedor();
                System.out.println(vencedor.getNome());
            }
        }
    }

    public static Voto votando(ArrayList<Pessoa> candidatos) {
        var scan = new Scanner(System.in);
        System.out.print("Eleitor: ");
        String nome = scan.next() + scan.nextLine();
        System.out.println("Candidato: ");
        String candidato = scan.next() + scan.nextLine();

        Pessoa votante = new Pessoa();
        votante.setNome(nome);

        Pessoa politico = candidatos.get(0);
        if (candidato.equals("Paulo Maluf"))
            politico = candidatos.get(1);
        else if (candidato.equals("Franco Montoro"))
            politico = candidatos.get(2);

        Voto v = new Voto();
        v.setDataHora(LocalDateTime.now());
        v.setCandidato(politico);
        v.setEleitor(votante);
        return v;
    }
}
