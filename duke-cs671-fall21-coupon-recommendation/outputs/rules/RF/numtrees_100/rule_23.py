def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Bar", "instances": 10, "metric_value": 1.0, "depth": 1}
	if obj[14]<=1.0:
		# {"feature": "Maritalstatus", "instances": 7, "metric_value": 0.8631, "depth": 2}
		if obj[9]<=3:
			# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[1]<=1:
				return 'False'
			elif obj[1]>1:
				# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]<=0:
					return 'False'
				elif obj[0]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[9]>3:
			return 'True'
		else: return 'True'
	elif obj[14]>1.0:
		return 'True'
	else: return 'True'