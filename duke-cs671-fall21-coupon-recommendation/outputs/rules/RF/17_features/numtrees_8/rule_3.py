def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9309, "depth": 1}
	if obj[3]>1:
		# {"feature": "Coupon_validity", "instances": 96, "metric_value": 0.8427, "depth": 2}
		if obj[4]<=0:
			# {"feature": "Distance", "instances": 52, "metric_value": 0.6194, "depth": 3}
			if obj[16]<=2:
				# {"feature": "Restaurant20to50", "instances": 51, "metric_value": 0.577, "depth": 4}
				if obj[14]<=1.0:
					# {"feature": "Occupation", "instances": 32, "metric_value": 0.7579, "depth": 5}
					if obj[10]<=8:
						# {"feature": "Bar", "instances": 25, "metric_value": 0.5294, "depth": 6}
						if obj[12]>0.0:
							return 'True'
						elif obj[12]<=0.0:
							# {"feature": "Income", "instances": 10, "metric_value": 0.8813, "depth": 7}
							if obj[11]>3:
								return 'True'
							elif obj[11]<=3:
								# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[2]>0:
									# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[5]>0:
										return 'True'
									elif obj[5]<=0:
										return 'False'
									else: return 'False'
								elif obj[2]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[10]>8:
						# {"feature": "Income", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[11]<=4:
							# {"feature": "Maritalstatus", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[7]>0:
								return 'True'
							elif obj[7]<=0:
								return 'False'
							else: return 'False'
						elif obj[11]>4:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[14]>1.0:
					return 'True'
				else: return 'True'
			elif obj[16]>2:
				return 'False'
			else: return 'False'
		elif obj[4]>0:
			# {"feature": "Time", "instances": 44, "metric_value": 0.976, "depth": 3}
			if obj[2]<=1:
				# {"feature": "Income", "instances": 27, "metric_value": 0.9911, "depth": 4}
				if obj[11]<=6:
					# {"feature": "Maritalstatus", "instances": 23, "metric_value": 0.9986, "depth": 5}
					if obj[7]<=1:
						# {"feature": "Coffeehouse", "instances": 21, "metric_value": 0.9852, "depth": 6}
						if obj[13]<=2.0:
							# {"feature": "Bar", "instances": 20, "metric_value": 0.971, "depth": 7}
							if obj[12]<=2.0:
								# {"feature": "Education", "instances": 18, "metric_value": 0.9911, "depth": 8}
								if obj[9]>0:
									# {"feature": "Distance", "instances": 10, "metric_value": 0.8813, "depth": 9}
									if obj[16]>1:
										return 'True'
									elif obj[16]<=1:
										# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[6]<=2:
											# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[0]<=1:
												return 'True'
											elif obj[0]>1:
												return 'False'
											else: return 'False'
										elif obj[6]>2:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[9]<=0:
									# {"feature": "Age", "instances": 8, "metric_value": 0.9544, "depth": 9}
									if obj[6]<=4:
										# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[0]<=2:
											return 'False'
										elif obj[0]>2:
											return 'True'
										else: return 'True'
									elif obj[6]>4:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[12]>2.0:
								return 'True'
							else: return 'True'
						elif obj[13]>2.0:
							return 'False'
						else: return 'False'
					elif obj[7]>1:
						return 'False'
					else: return 'False'
				elif obj[11]>6:
					return 'False'
				else: return 'False'
			elif obj[2]>1:
				# {"feature": "Income", "instances": 17, "metric_value": 0.6723, "depth": 4}
				if obj[11]>2:
					return 'True'
				elif obj[11]<=2:
					# {"feature": "Gender", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[5]<=0:
						# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[6]>0:
							return 'True'
						elif obj[6]<=0:
							return 'False'
						else: return 'False'
					elif obj[5]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[3]<=1:
		# {"feature": "Bar", "instances": 31, "metric_value": 0.9812, "depth": 2}
		if obj[12]<=1.0:
			# {"feature": "Age", "instances": 17, "metric_value": 0.6723, "depth": 3}
			if obj[6]>2:
				return 'False'
			elif obj[6]<=2:
				# {"feature": "Gender", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[5]>0:
					# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Coupon_validity", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[4]>0:
							# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[1]<=0:
								return 'False'
							elif obj[1]>0:
								return 'True'
							else: return 'True'
						elif obj[4]<=0:
							return 'True'
						else: return 'True'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				elif obj[5]<=0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[12]>1.0:
			# {"feature": "Distance", "instances": 14, "metric_value": 0.8631, "depth": 3}
			if obj[16]>1:
				# {"feature": "Occupation", "instances": 12, "metric_value": 0.65, "depth": 4}
				if obj[10]>5:
					# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[0]>1:
						# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[2]<=2:
							return 'True'
						elif obj[2]>2:
							return 'False'
						else: return 'False'
					elif obj[0]<=1:
						return 'False'
					else: return 'False'
				elif obj[10]<=5:
					return 'True'
				else: return 'True'
			elif obj[16]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
