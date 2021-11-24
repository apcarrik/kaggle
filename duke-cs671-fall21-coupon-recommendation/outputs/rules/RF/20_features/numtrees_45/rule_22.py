def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Income", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[13]>2:
		# {"feature": "Age", "instances": 16, "metric_value": 0.5436, "depth": 2}
		if obj[8]>2:
			return 'True'
		elif obj[8]<=2:
			# {"feature": "Maritalstatus", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[9]>0:
				return 'True'
			elif obj[9]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[13]<=2:
		# {"feature": "Driving_to", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[0]>0:
			return 'False'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
