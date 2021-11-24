def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Weather", "instances": 41, "metric_value": 0.965, "depth": 1}
	if obj[2]<=0:
		# {"feature": "Coupon_validity", "instances": 32, "metric_value": 0.8571, "depth": 2}
		if obj[6]<=0:
			# {"feature": "Driving_to", "instances": 18, "metric_value": 0.9911, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Distance", "instances": 14, "metric_value": 0.8631, "depth": 4}
				if obj[20]<=1:
					# {"feature": "Occupation", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[12]>7:
						return 'False'
					elif obj[12]<=7:
						return 'True'
					else: return 'True'
				elif obj[20]>1:
					return 'True'
				else: return 'True'
			elif obj[0]>1:
				return 'False'
			else: return 'False'
		elif obj[6]>0:
			# {"feature": "Income", "instances": 14, "metric_value": 0.3712, "depth": 3}
			if obj[13]>2:
				return 'True'
			elif obj[13]<=2:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]<=0:
					return 'True'
				elif obj[1]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[2]>0:
		# {"feature": "Income", "instances": 9, "metric_value": 0.7642, "depth": 2}
		if obj[13]>2:
			return 'False'
		elif obj[13]<=2:
			# {"feature": "Carryaway", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[16]>2.0:
				return 'False'
			elif obj[16]<=2.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
