def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Coffeehouse", "instances": 85, "metric_value": 0.9951, "depth": 1}
	if obj[9]>1.0:
		# {"feature": "Distance", "instances": 44, "metric_value": 0.976, "depth": 2}
		if obj[12]>1:
			# {"feature": "Time", "instances": 29, "metric_value": 0.9923, "depth": 3}
			if obj[1]>0:
				# {"feature": "Restaurant20to50", "instances": 26, "metric_value": 0.9612, "depth": 4}
				if obj[10]<=2.0:
					# {"feature": "Education", "instances": 24, "metric_value": 0.9183, "depth": 5}
					if obj[6]>0:
						# {"feature": "Children", "instances": 14, "metric_value": 0.5917, "depth": 6}
						if obj[5]>0:
							# {"feature": "Bar", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[8]<=0.0:
								return 'False'
							elif obj[8]>0.0:
								return 'True'
							else: return 'True'
						elif obj[5]<=0:
							return 'False'
						else: return 'False'
					elif obj[6]<=0:
						# {"feature": "Coupon", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[2]<=2:
							# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[0]<=2:
								# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[4]>0:
									return 'False'
								elif obj[4]<=0:
									return 'True'
								else: return 'True'
							elif obj[0]>2:
								return 'True'
							else: return 'True'
						elif obj[2]>2:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[10]>2.0:
					return 'True'
				else: return 'True'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		elif obj[12]<=1:
			# {"feature": "Direction_same", "instances": 15, "metric_value": 0.5665, "depth": 3}
			if obj[11]<=0:
				return 'True'
			elif obj[11]>0:
				# {"feature": "Occupation", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[7]<=5:
					return 'False'
				elif obj[7]>5:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[9]<=1.0:
		# {"feature": "Coupon", "instances": 41, "metric_value": 0.9012, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Occupation", "instances": 29, "metric_value": 0.9923, "depth": 3}
			if obj[7]<=7:
				# {"feature": "Time", "instances": 19, "metric_value": 0.8315, "depth": 4}
				if obj[1]>1:
					# {"feature": "Education", "instances": 14, "metric_value": 0.9403, "depth": 5}
					if obj[6]>0:
						# {"feature": "Age", "instances": 10, "metric_value": 1.0, "depth": 6}
						if obj[4]>0:
							# {"feature": "Gender", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[3]>0:
								# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[8]<=0.0:
									# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[5]>0:
										# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[0]<=3:
											# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[12]<=2:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[5]<=0:
										return 'False'
									else: return 'False'
								elif obj[8]>0.0:
									return 'True'
								else: return 'True'
							elif obj[3]<=0:
								return 'True'
							else: return 'True'
						elif obj[4]<=0:
							return 'False'
						else: return 'False'
					elif obj[6]<=0:
						return 'False'
					else: return 'False'
				elif obj[1]<=1:
					return 'False'
				else: return 'False'
			elif obj[7]>7:
				# {"feature": "Education", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[6]>0:
					# {"feature": "Passanger", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[0]<=1:
						return 'True'
					elif obj[0]>1:
						# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[4]<=1:
							return 'True'
						elif obj[4]>1:
							# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]>2:
								return 'True'
							elif obj[1]<=2:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				elif obj[6]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[2]>3:
			return 'False'
		else: return 'False'
	else: return 'False'
