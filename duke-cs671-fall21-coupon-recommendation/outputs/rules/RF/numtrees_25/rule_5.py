def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Education", "instances": 41, "metric_value": 0.9789, "depth": 1}
	if obj[11]>0:
		# {"feature": "Income", "instances": 31, "metric_value": 0.9992, "depth": 2}
		if obj[13]<=6:
			# {"feature": "Temperature", "instances": 27, "metric_value": 0.9751, "depth": 3}
			if obj[3]<=55:
				# {"feature": "Coupon", "instances": 15, "metric_value": 0.971, "depth": 4}
				if obj[5]<=2:
					# {"feature": "Passanger", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=1:
						# {"feature": "Carryaway", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[16]<=3.0:
							return 'False'
						elif obj[16]>3.0:
							return 'True'
						else: return 'True'
					elif obj[1]>1:
						return 'True'
					else: return 'True'
				elif obj[5]>2:
					return 'True'
				else: return 'True'
			elif obj[3]>55:
				# {"feature": "Bar", "instances": 12, "metric_value": 0.65, "depth": 4}
				if obj[14]<=1.0:
					# {"feature": "Passanger", "instances": 11, "metric_value": 0.4395, "depth": 5}
					if obj[1]<=2:
						return 'False'
					elif obj[1]>2:
						# {"feature": "Coupon_validity", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[6]>0:
							return 'False'
						elif obj[6]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[14]>1.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[13]>6:
			return 'True'
		else: return 'True'
	elif obj[11]<=0:
		# {"feature": "Age", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[8]<=6:
			return 'True'
		elif obj[8]>6:
			# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0]<=0:
				return 'True'
			elif obj[0]>0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
