using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace SomeNamespace
{
	[Table("contract")]
	public class Contract
	{
		[Key] [Column("id")] public long? Id{get; set;}
		[Column("id_anno")] public long? IdAnno{get; set;}
		[Column("id_contract")] public long? IdContract{get; set;}
		[Column("number_contract")] public string NumberContract{get; set;}
		[Column("id_tf")] public long? IdTf{get; set;}
		[Column("amount_sum")] public double? AmountSum{get; set;}
		[Column("2)")] public UnknownType 2){get; set;}
		[Column("bin_supplier")] public long? BinSupplier{get; set;}
		[Column("id_status")] public long? IdStatus{get; set;}
		[Column("dt_start")] public DateTime? DtStart{get; set;}
		[Column("dt_end")] public DateTime? DtEnd{get; set;}
		[Column("id_type")] public long? IdType{get; set;}
		[Column("relevance_date")] public DateTime? RelevanceDate{get; set;}
		[Column("add_info")] public UnknownType AddInfo{get; set;}
		[Column("bin_customer")] public long? BinCustomer{get; set;}
		[Column("fin_year")] public DateTime? FinYear{get; set;}
		[Column("constraint")] public UnknownType Constraint{get; set;}
		[Column("id_tf)")] public UnknownType IdTf){get; set;}
		[Column("constraint")] public UnknownType Constraint{get; set;}
		[Column("id_tf)")] public UnknownType IdTf){get; set;}
		[Column("id_tf)")] public UnknownType IdTf){get; set;}
		
	}
}
