def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[11]<=1:
		# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.874, "depth": 2}
		if obj[15]>0.0:
			# {"feature": "Occupation", "instances": 14, "metric_value": 0.5917, "depth": 3}
			if obj[12]<=12:
				return 'True'
			elif obj[12]>12:
				return 'False'
			else: return 'False'
		elif obj[15]<=0.0:
			return 'False'
		else: return 'False'
	elif obj[11]>1:
		# {"feature": "Coupon_validity", "instances": 17, "metric_value": 0.874, "depth": 2}
		if obj[6]<=0:
			# {"feature": "Income", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[13]>2:
				# {"feature": "Driving_to", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Age", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[8]>0:
						return 'True'
					elif obj[8]<=0:
						return 'False'
					else: return 'False'
				elif obj[0]>1:
					return 'False'
				else: return 'False'
			elif obj[13]<=2:
				return 'False'
			else: return 'False'
		elif obj[6]>0:
			return 'False'
		else: return 'False'
	else: return 'False'
