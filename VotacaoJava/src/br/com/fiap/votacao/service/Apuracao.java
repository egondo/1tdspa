package br.com.fiap.votacao.service;

import br.com.fiap.votacao.model.Pessoa;
import br.com.fiap.votacao.model.Voto;

import java.util.ArrayList;

public class Apuracao {

    private ArrayList<Voto> votos = new ArrayList<>();
    private ArrayList<Pessoa> candidatos = new ArrayList<>();

    public ArrayList<Pessoa> getCandidatos() {
        return candidatos;
    }

    public void addVoto(Voto v) {
        //verificar se a pessoa contida no voto já votou
        votos.add(v);
    }

    public void addCandidato(Pessoa pes) {
        //verificar se nao existem 2 pessoas iguais
        candidatos.add(pes);
    }

    public Pessoa vencedor() {
        Pessoa winner = null;
        int votosWinner = 0;


        for(Pessoa p : candidatos) {
            int auxVotos = 0;
            for(Voto v : votos) {
                if (v.getCandidato().getId() == p.getId())
                    auxVotos++;
            }
            if (auxVotos > votosWinner) {
                votosWinner = auxVotos;
                winner = p;
            }
        }
        return winner;
    }
}
