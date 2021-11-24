def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Age", "instances": 85, "metric_value": 0.9991, "depth": 1}
	if obj[8]>0:
		# {"feature": "Coffeehouse", "instances": 73, "metric_value": 0.9966, "depth": 2}
		if obj[15]>1.0:
			# {"feature": "Coupon_validity", "instances": 39, "metric_value": 0.9612, "depth": 3}
			if obj[6]>0:
				# {"feature": "Distance", "instances": 24, "metric_value": 0.995, "depth": 4}
				if obj[19]<=2:
					# {"feature": "Occupation", "instances": 19, "metric_value": 0.9819, "depth": 5}
					if obj[12]<=7:
						# {"feature": "Gender", "instances": 15, "metric_value": 0.9968, "depth": 6}
						if obj[7]<=0:
							# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[1]<=2:
								# {"feature": "Maritalstatus", "instances": 7, "metric_value": 0.5917, "depth": 8}
								if obj[9]<=1:
									return 'True'
								elif obj[9]>1:
									return 'False'
								else: return 'False'
							elif obj[1]>2:
								return 'False'
							else: return 'False'
						elif obj[7]>0:
							# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[1]<=2:
								return 'False'
							elif obj[1]>2:
								# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[9]>2:
									return 'False'
								elif obj[9]<=2:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'False'
					elif obj[12]>7:
						return 'True'
					else: return 'True'
				elif obj[19]>2:
					return 'False'
				else: return 'False'
			elif obj[6]<=0:
				# {"feature": "Occupation", "instances": 15, "metric_value": 0.5665, "depth": 4}
				if obj[12]<=11:
					return 'True'
				elif obj[12]>11:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[15]<=1.0:
			# {"feature": "Income", "instances": 34, "metric_value": 0.874, "depth": 3}
			if obj[13]<=6:
				# {"feature": "Education", "instances": 29, "metric_value": 0.7355, "depth": 4}
				if obj[11]>0:
					# {"feature": "Occupation", "instances": 20, "metric_value": 0.8813, "depth": 5}
					if obj[12]>2:
						# {"feature": "Restaurantlessthan20", "instances": 15, "metric_value": 0.7219, "depth": 6}
						if obj[16]<=2.0:
							# {"feature": "Coupon_validity", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Maritalstatus", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[9]<=1:
									return 'False'
								elif obj[9]>1:
									return 'True'
								else: return 'True'
							elif obj[6]>0:
								return 'True'
							else: return 'True'
						elif obj[16]>2.0:
							return 'False'
						else: return 'False'
					elif obj[12]<=2:
						# {"feature": "Weather", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[2]>0:
							# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[3]>30:
								return 'False'
							elif obj[3]<=30:
								return 'True'
							else: return 'True'
						elif obj[2]<=0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[11]<=0:
					return 'False'
				else: return 'False'
			elif obj[13]>6:
				# {"feature": "Maritalstatus", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[9]>0:
					return 'True'
				elif obj[9]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[8]<=0:
		# {"feature": "Income", "instances": 12, "metric_value": 0.65, "depth": 2}
		if obj[13]<=6:
			# {"feature": "Passanger", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[1]<=1:
				return 'True'
			elif obj[1]>1:
				# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3]>30:
					# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[5]<=2:
						return 'False'
					elif obj[5]>2:
						return 'True'
					else: return 'True'
				elif obj[3]<=30:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[13]>6:
			return 'False'
		else: return 'False'
	else: return 'True'
