def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 1.0, "depth": 1}
	if obj[5]>0:
		# {"feature": "Coupon_validity", "instances": 103, "metric_value": 0.9846, "depth": 2}
		if obj[6]>0:
			# {"feature": "Weather", "instances": 58, "metric_value": 0.9923, "depth": 3}
			if obj[2]<=0:
				# {"feature": "Occupation", "instances": 44, "metric_value": 0.9985, "depth": 4}
				if obj[12]<=18:
					# {"feature": "Income", "instances": 39, "metric_value": 0.9957, "depth": 5}
					if obj[13]>2:
						# {"feature": "Maritalstatus", "instances": 29, "metric_value": 0.9923, "depth": 6}
						if obj[9]<=2:
							# {"feature": "Children", "instances": 26, "metric_value": 0.9612, "depth": 7}
							if obj[10]>0:
								# {"feature": "Time", "instances": 14, "metric_value": 0.7496, "depth": 8}
								if obj[4]<=1:
									# {"feature": "Direction_same", "instances": 7, "metric_value": 0.9852, "depth": 9}
									if obj[18]<=0:
										# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[8]>0:
											return 'False'
										elif obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[18]>0:
										return 'True'
									else: return 'True'
								elif obj[4]>1:
									return 'True'
								else: return 'True'
							elif obj[10]<=0:
								# {"feature": "Time", "instances": 12, "metric_value": 0.9799, "depth": 8}
								if obj[4]>0:
									# {"feature": "Education", "instances": 9, "metric_value": 0.7642, "depth": 9}
									if obj[11]>1:
										return 'False'
									elif obj[11]<=1:
										# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[0]>0:
											return 'True'
										elif obj[0]<=0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[4]<=0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[9]>2:
							return 'False'
						else: return 'False'
					elif obj[13]<=2:
						# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[15]<=2.0:
							return 'False'
						elif obj[15]>2.0:
							# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[8]>1:
								return 'True'
							elif obj[8]<=1:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				elif obj[12]>18:
					return 'True'
				else: return 'True'
			elif obj[2]>0:
				# {"feature": "Education", "instances": 14, "metric_value": 0.7496, "depth": 4}
				if obj[11]>1:
					return 'False'
				elif obj[11]<=1:
					# {"feature": "Driving_to", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[0]>0:
						# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[8]<=4:
							return 'True'
						elif obj[8]>4:
							return 'False'
						else: return 'False'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[6]<=0:
			# {"feature": "Passanger", "instances": 45, "metric_value": 0.8366, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Education", "instances": 34, "metric_value": 0.9367, "depth": 4}
				if obj[11]<=3:
					# {"feature": "Income", "instances": 29, "metric_value": 0.9784, "depth": 5}
					if obj[13]<=3:
						# {"feature": "Time", "instances": 15, "metric_value": 0.971, "depth": 6}
						if obj[4]>0:
							# {"feature": "Temperature", "instances": 12, "metric_value": 0.8113, "depth": 7}
							if obj[3]<=55:
								return 'False'
							elif obj[3]>55:
								# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[17]>1.0:
									return 'False'
								elif obj[17]<=1.0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[4]<=0:
							return 'True'
						else: return 'True'
					elif obj[13]>3:
						# {"feature": "Age", "instances": 14, "metric_value": 0.7496, "depth": 6}
						if obj[8]<=4:
							# {"feature": "Weather", "instances": 11, "metric_value": 0.4395, "depth": 7}
							if obj[2]<=1:
								return 'True'
							elif obj[2]>1:
								# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=0:
									return 'False'
								elif obj[7]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[8]>4:
							# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[0]>1:
								return 'False'
							elif obj[0]<=1:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[11]>3:
					return 'True'
				else: return 'True'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[5]<=0:
		# {"feature": "Occupation", "instances": 24, "metric_value": 0.65, "depth": 2}
		if obj[12]>2:
			return 'False'
		elif obj[12]<=2:
			# {"feature": "Restaurantlessthan20", "instances": 8, "metric_value": 1.0, "depth": 3}
			if obj[16]<=2.0:
				return 'False'
			elif obj[16]>2.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
