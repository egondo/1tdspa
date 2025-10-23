package br.com.fiap.votacao.model;

import java.time.LocalDateTime;

public class Voto {

    private int id;
    private Pessoa eleitor;
    private Pessoa candidato;
    private LocalDateTime dataHora;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Pessoa getEleitor() {
        return eleitor;
    }

    public void setEleitor(Pessoa eleitor) {
        this.eleitor = eleitor;
    }

    public Pessoa getCandidato() {
        return candidato;
    }

    public void setCandidato(Pessoa candidato) {
        this.candidato = candidato;
    }

    public LocalDateTime getDataHora() {
        return dataHora;
    }

    public void setDataHora(LocalDateTime dataHora) {
        this.dataHora = dataHora;
    }
}
