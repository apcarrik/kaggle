def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Driving_to", "instances": 127, "metric_value": 0.9899, "depth": 1}
	if obj[0]>0:
		# {"feature": "Carryaway", "instances": 66, "metric_value": 0.9894, "depth": 2}
		if obj[16]<=3.0:
			# {"feature": "Temperature", "instances": 61, "metric_value": 0.9983, "depth": 3}
			if obj[3]<=55:
				# {"feature": "Income", "instances": 38, "metric_value": 0.9495, "depth": 4}
				if obj[13]<=6:
					# {"feature": "Passanger", "instances": 34, "metric_value": 0.874, "depth": 5}
					if obj[1]>0:
						# {"feature": "Bar", "instances": 31, "metric_value": 0.7706, "depth": 6}
						if obj[14]>0.0:
							# {"feature": "Weather", "instances": 19, "metric_value": 0.9495, "depth": 7}
							if obj[2]<=1:
								# {"feature": "Occupation", "instances": 11, "metric_value": 0.684, "depth": 8}
								if obj[12]<=14:
									return 'False'
								elif obj[12]>14:
									# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[5]<=0:
										return 'True'
									elif obj[5]>0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[2]>1:
								# {"feature": "Coupon", "instances": 8, "metric_value": 0.9544, "depth": 8}
								if obj[5]>2:
									return 'True'
								elif obj[5]<=2:
									# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[8]<=2:
										return 'False'
									elif obj[8]>2:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						elif obj[14]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				elif obj[13]>6:
					return 'True'
				else: return 'True'
			elif obj[3]>55:
				# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.9321, "depth": 4}
				if obj[15]<=2.0:
					# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.9975, "depth": 5}
					if obj[18]<=1.0:
						# {"feature": "Time", "instances": 13, "metric_value": 0.9612, "depth": 6}
						if obj[4]>0:
							# {"feature": "Restaurantlessthan20", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[17]<=2.0:
								return 'True'
							elif obj[17]>2.0:
								return 'False'
							else: return 'False'
						elif obj[4]<=0:
							return 'False'
						else: return 'False'
					elif obj[18]>1.0:
						return 'True'
					else: return 'True'
				elif obj[15]>2.0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[16]>3.0:
			return 'False'
		else: return 'False'
	elif obj[0]<=0:
		# {"feature": "Education", "instances": 61, "metric_value": 0.8949, "depth": 2}
		if obj[11]<=3:
			# {"feature": "Bar", "instances": 54, "metric_value": 0.9357, "depth": 3}
			if obj[14]<=1.0:
				# {"feature": "Coupon", "instances": 38, "metric_value": 0.992, "depth": 4}
				if obj[5]>0:
					# {"feature": "Coffeehouse", "instances": 33, "metric_value": 0.9457, "depth": 5}
					if obj[15]<=3.0:
						# {"feature": "Restaurantlessthan20", "instances": 31, "metric_value": 0.9072, "depth": 6}
						if obj[17]>1.0:
							# {"feature": "Passanger", "instances": 25, "metric_value": 0.795, "depth": 7}
							if obj[1]>1:
								# {"feature": "Maritalstatus", "instances": 13, "metric_value": 0.3912, "depth": 8}
								if obj[9]<=1:
									return 'True'
								elif obj[9]>1:
									# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[2]<=0:
										return 'True'
									elif obj[2]>0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[1]<=1:
								# {"feature": "Occupation", "instances": 12, "metric_value": 0.9799, "depth": 8}
								if obj[12]<=14:
									# {"feature": "Carryaway", "instances": 10, "metric_value": 0.8813, "depth": 9}
									if obj[16]>2.0:
										# {"feature": "Income", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[13]<=3:
											return 'False'
										elif obj[13]>3:
											return 'True'
										else: return 'True'
									elif obj[16]<=2.0:
										return 'True'
									else: return 'True'
								elif obj[12]>14:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[17]<=1.0:
							# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[1]>0:
								# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[4]>2:
									return 'False'
								elif obj[4]<=2:
									# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[6]>0:
										return 'False'
									elif obj[6]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[1]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[15]>3.0:
						return 'False'
					else: return 'False'
				elif obj[5]<=0:
					return 'False'
				else: return 'False'
			elif obj[14]>1.0:
				# {"feature": "Income", "instances": 16, "metric_value": 0.5436, "depth": 4}
				if obj[13]>1:
					return 'True'
				elif obj[13]<=1:
					# {"feature": "Temperature", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[3]<=55:
						return 'False'
					elif obj[3]>55:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[11]>3:
			return 'True'
		else: return 'True'
	else: return 'True'
