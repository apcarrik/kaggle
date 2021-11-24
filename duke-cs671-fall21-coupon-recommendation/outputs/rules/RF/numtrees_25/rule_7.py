def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Passanger", "instances": 41, "metric_value": 0.9996, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Coupon_validity", "instances": 31, "metric_value": 0.9383, "depth": 2}
		if obj[6]<=0:
			# {"feature": "Bar", "instances": 19, "metric_value": 0.998, "depth": 3}
			if obj[14]<=1.0:
				# {"feature": "Income", "instances": 11, "metric_value": 0.8454, "depth": 4}
				if obj[13]>3:
					return 'False'
				elif obj[13]<=3:
					# {"feature": "Children", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[10]>0:
						return 'True'
					elif obj[10]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[14]>1.0:
				# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[15]<=3.0:
					return 'True'
				elif obj[15]>3.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[6]>0:
			# {"feature": "Weather", "instances": 12, "metric_value": 0.4138, "depth": 3}
			if obj[2]<=1:
				return 'False'
			elif obj[2]>1:
				# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[8]<=1:
					return 'True'
				elif obj[8]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[1]>2:
		return 'True'
	else: return 'True'
