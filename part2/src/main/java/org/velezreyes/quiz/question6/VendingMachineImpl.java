package org.velezreyes.quiz.question6;

public class VendingMachineImpl {

  public static VendingMachine getInstance() {

      return new VendingMachine() {
      Double money = 0.0;
      @Override
      public void insertQuarter() {
          money += 0.25;
      }
      @Override
      public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {


        if("ScottCola".equals(name) && money < 0.75){
          throw new NotEnoughMoneyException();
        }
        if("KarenTea".equals(name) && money < 1.0){
          throw new NotEnoughMoneyException();
        }
        if (!("ScottCola".equals(name) || "KarenTea".equals(name))){
          throw new UnknownDrinkException();
        }

        money = 0.0;


        return retunrDrink(name);

      }
      public Drink retunrDrink(String name){
        return new Drink() {
          @Override
          public String getName() {
            switch (name){
              case "ScottCola":
                return "ScottCola";
              case "KarenTea":
                return "KarenTea";
            }
            return null;
          }

          @Override
          public boolean isFizzy() {
            switch (name){
              case "ScottCola":
                return true;
              case "KarenTea":
                return false;
            }
            return false;
          }
        };
      }

    };
  }
}
