def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Time", "instances": 127, "metric_value": 0.9621, "depth": 1}
	if obj[4]<=2:
		# {"feature": "Carryaway", "instances": 80, "metric_value": 1.0, "depth": 2}
		if obj[16]<=2.0:
			# {"feature": "Maritalstatus", "instances": 43, "metric_value": 0.9523, "depth": 3}
			if obj[9]<=1:
				# {"feature": "Coupon", "instances": 37, "metric_value": 0.878, "depth": 4}
				if obj[5]<=3:
					# {"feature": "Education", "instances": 24, "metric_value": 0.9799, "depth": 5}
					if obj[11]>1:
						# {"feature": "Income", "instances": 16, "metric_value": 0.9887, "depth": 6}
						if obj[13]>0:
							# {"feature": "Coupon_validity", "instances": 13, "metric_value": 0.8905, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Bar", "instances": 9, "metric_value": 0.5033, "depth": 8}
								if obj[14]>-1.0:
									return 'True'
								elif obj[14]<=-1.0:
									# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[0]<=1:
										return 'False'
									elif obj[0]>1:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[6]>0:
								# {"feature": "Driving_to", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[0]<=1:
									return 'False'
								elif obj[0]>1:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[13]<=0:
							return 'False'
						else: return 'False'
					elif obj[11]<=1:
						# {"feature": "Age", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[8]<=3:
							return 'False'
						elif obj[8]>3:
							# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]>0:
								return 'False'
							elif obj[0]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'False'
				elif obj[5]>3:
					# {"feature": "Age", "instances": 13, "metric_value": 0.3912, "depth": 5}
					if obj[8]<=5:
						return 'False'
					elif obj[8]>5:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[9]>1:
				# {"feature": "Temperature", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[3]>55:
					return 'True'
				elif obj[3]<=55:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[16]>2.0:
			# {"feature": "Passanger", "instances": 37, "metric_value": 0.9353, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Income", "instances": 22, "metric_value": 1.0, "depth": 4}
				if obj[13]<=6:
					# {"feature": "Maritalstatus", "instances": 19, "metric_value": 0.9819, "depth": 5}
					if obj[9]>0:
						# {"feature": "Temperature", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[3]>30:
							return 'False'
						elif obj[3]<=30:
							# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[0]>0:
								return 'True'
							elif obj[0]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[9]<=0:
						# {"feature": "Driving_to", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Coffeehouse", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[15]>1.0:
								return 'True'
							elif obj[15]<=1.0:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[13]>6:
					return 'True'
				else: return 'True'
			elif obj[1]>1:
				# {"feature": "Age", "instances": 15, "metric_value": 0.5665, "depth": 4}
				if obj[8]<=6:
					# {"feature": "Income", "instances": 14, "metric_value": 0.3712, "depth": 5}
					if obj[13]>0:
						return 'True'
					elif obj[13]<=0:
						return 'False'
					else: return 'False'
				elif obj[8]>6:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[4]>2:
		# {"feature": "Coupon_validity", "instances": 47, "metric_value": 0.7046, "depth": 2}
		if obj[6]>0:
			# {"feature": "Income", "instances": 28, "metric_value": 0.8631, "depth": 3}
			if obj[13]<=4:
				# {"feature": "Restaurantlessthan20", "instances": 19, "metric_value": 0.9819, "depth": 4}
				if obj[17]<=2.0:
					# {"feature": "Temperature", "instances": 13, "metric_value": 0.7793, "depth": 5}
					if obj[3]>55:
						# {"feature": "Gender", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[7]<=0:
							# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[14]>0.0:
								return 'False'
							elif obj[14]<=0.0:
								return 'True'
							else: return 'True'
						elif obj[7]>0:
							return 'True'
						else: return 'True'
					elif obj[3]<=55:
						return 'True'
					else: return 'True'
				elif obj[17]>2.0:
					# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[15]<=2.0:
						return 'False'
					elif obj[15]>2.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[13]>4:
				return 'True'
			else: return 'True'
		elif obj[6]<=0:
			# {"feature": "Restaurantlessthan20", "instances": 19, "metric_value": 0.2975, "depth": 3}
			if obj[17]>0.0:
				return 'True'
			elif obj[17]<=0.0:
				# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[7]>0:
					return 'False'
				elif obj[7]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	else: return 'True'
