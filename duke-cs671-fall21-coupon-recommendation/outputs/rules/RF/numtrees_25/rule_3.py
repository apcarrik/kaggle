def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Distance", "instances": 41, "metric_value": 0.9892, "depth": 1}
	if obj[20]>1:
		# {"feature": "Income", "instances": 22, "metric_value": 0.9024, "depth": 2}
		if obj[13]<=6:
			# {"feature": "Occupation", "instances": 19, "metric_value": 0.9495, "depth": 3}
			if obj[12]<=12:
				# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.874, "depth": 4}
				if obj[15]<=1.0:
					# {"feature": "Direction_same", "instances": 13, "metric_value": 0.9612, "depth": 5}
					if obj[19]<=0:
						# {"feature": "Coupon_validity", "instances": 11, "metric_value": 0.994, "depth": 6}
						if obj[6]<=0:
							# {"feature": "Driving_to", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Weather", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[2]<=0:
									return 'False'
								elif obj[2]>0:
									return 'True'
								else: return 'True'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						elif obj[6]>0:
							# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[3]<=55:
								return 'True'
							elif obj[3]>55:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[19]>0:
						return 'False'
					else: return 'False'
				elif obj[15]>1.0:
					return 'False'
				else: return 'False'
			elif obj[12]>12:
				return 'True'
			else: return 'True'
		elif obj[13]>6:
			return 'False'
		else: return 'False'
	elif obj[20]<=1:
		# {"feature": "Gender", "instances": 19, "metric_value": 0.6292, "depth": 2}
		if obj[7]>0:
			return 'True'
		elif obj[7]<=0:
			# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[18]>0.0:
				# {"feature": "Carryaway", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[16]>1.0:
					return 'True'
				elif obj[16]<=1.0:
					return 'False'
				else: return 'False'
			elif obj[18]<=0.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
