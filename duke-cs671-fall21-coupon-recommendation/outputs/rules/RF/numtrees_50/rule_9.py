def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Coupon", "instances": 20, "metric_value": 0.971, "depth": 1}
	if obj[5]>1:
		# {"feature": "Age", "instances": 13, "metric_value": 0.6194, "depth": 2}
		if obj[8]>3:
			# {"feature": "Time", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[4]<=2:
				# {"feature": "Maritalstatus", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[9]>0:
					return 'True'
				elif obj[9]<=0:
					return 'False'
				else: return 'False'
			elif obj[4]>2:
				return 'False'
			else: return 'False'
		elif obj[8]<=3:
			return 'True'
		else: return 'True'
	elif obj[5]<=1:
		# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[1]>0:
			return 'False'
		elif obj[1]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
