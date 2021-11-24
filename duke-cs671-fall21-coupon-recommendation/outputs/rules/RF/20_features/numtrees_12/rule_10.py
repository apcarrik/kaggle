def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Restaurant20to50", "instances": 85, "metric_value": 0.9919, "depth": 1}
	if obj[17]<=1.0:
		# {"feature": "Coupon", "instances": 61, "metric_value": 0.9983, "depth": 2}
		if obj[5]>1:
			# {"feature": "Restaurantlessthan20", "instances": 41, "metric_value": 0.9892, "depth": 3}
			if obj[16]>0.0:
				# {"feature": "Passanger", "instances": 37, "metric_value": 0.9995, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Time", "instances": 25, "metric_value": 0.971, "depth": 5}
					if obj[4]<=2:
						# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.874, "depth": 6}
						if obj[15]>1.0:
							# {"feature": "Distance", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[19]<=1:
								# {"feature": "Income", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[13]<=3:
									return 'False'
								elif obj[13]>3:
									return 'True'
								else: return 'True'
							elif obj[19]>1:
								return 'True'
							else: return 'True'
						elif obj[15]<=1.0:
							return 'False'
						else: return 'False'
					elif obj[4]>2:
						# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[11]>1:
							# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[12]<=11:
								return 'False'
							elif obj[12]>11:
								return 'True'
							else: return 'True'
						elif obj[11]<=1:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[1]>2:
					# {"feature": "Temperature", "instances": 12, "metric_value": 0.8113, "depth": 5}
					if obj[3]>55:
						# {"feature": "Age", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[8]<=3:
							# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[4]<=2:
								# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[12]>1:
									return 'True'
								elif obj[12]<=1:
									return 'False'
								else: return 'False'
							elif obj[4]>2:
								return 'False'
							else: return 'False'
						elif obj[8]>3:
							return 'True'
						else: return 'True'
					elif obj[3]<=55:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[16]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[5]<=1:
			# {"feature": "Bar", "instances": 20, "metric_value": 0.8813, "depth": 3}
			if obj[14]<=1.0:
				# {"feature": "Income", "instances": 17, "metric_value": 0.6723, "depth": 4}
				if obj[13]>4:
					return 'False'
				elif obj[13]<=4:
					# {"feature": "Time", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[4]>2:
						return 'False'
					elif obj[4]<=2:
						# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[8]<=6:
							return 'True'
						elif obj[8]>6:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[14]>1.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[17]>1.0:
		# {"feature": "Distance", "instances": 24, "metric_value": 0.8113, "depth": 2}
		if obj[19]<=2:
			# {"feature": "Income", "instances": 21, "metric_value": 0.5917, "depth": 3}
			if obj[13]>2:
				return 'True'
			elif obj[13]<=2:
				# {"feature": "Restaurantlessthan20", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[16]>2.0:
					# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[5]>0:
						return 'True'
					elif obj[5]<=0:
						return 'False'
					else: return 'False'
				elif obj[16]<=2.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[19]>2:
			return 'False'
		else: return 'False'
	else: return 'True'
