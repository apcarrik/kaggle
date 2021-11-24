def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Passanger", "instances": 85, "metric_value": 0.9999, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Occupation", "instances": 53, "metric_value": 0.9687, "depth": 2}
		if obj[6]>1:
			# {"feature": "Coffeehouse", "instances": 39, "metric_value": 0.8582, "depth": 3}
			if obj[8]>0.0:
				# {"feature": "Education", "instances": 33, "metric_value": 0.9183, "depth": 4}
				if obj[5]<=3:
					# {"feature": "Restaurant20to50", "instances": 32, "metric_value": 0.896, "depth": 5}
					if obj[9]<=2.0:
						# {"feature": "Age", "instances": 31, "metric_value": 0.8691, "depth": 6}
						if obj[4]>0:
							# {"feature": "Time", "instances": 28, "metric_value": 0.8113, "depth": 7}
							if obj[1]<=1:
								# {"feature": "Distance", "instances": 17, "metric_value": 0.9367, "depth": 8}
								if obj[11]<=2:
									# {"feature": "Coupon", "instances": 14, "metric_value": 0.9852, "depth": 9}
									if obj[2]>0:
										# {"feature": "Direction_same", "instances": 9, "metric_value": 0.9911, "depth": 10}
										if obj[10]<=0:
											# {"feature": "Bar", "instances": 7, "metric_value": 0.9852, "depth": 11}
											if obj[7]>-1.0:
												# {"feature": "Gender", "instances": 6, "metric_value": 1.0, "depth": 12}
												if obj[3]<=0:
													return 'False'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											elif obj[7]<=-1.0:
												return 'False'
											else: return 'False'
										elif obj[10]>0:
											return 'True'
										else: return 'True'
									elif obj[2]<=0:
										# {"feature": "Gender", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[3]>0:
											# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[7]<=0.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[10]<=1:
													return 'False'
												else: return 'False'
											elif obj[7]>0.0:
												return 'False'
											else: return 'False'
										elif obj[3]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[11]>2:
									return 'False'
								else: return 'False'
							elif obj[1]>1:
								# {"feature": "Coupon", "instances": 11, "metric_value": 0.4395, "depth": 8}
								if obj[2]>0:
									return 'False'
								elif obj[2]<=0:
									# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[3]<=0:
										return 'True'
									elif obj[3]>0:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'False'
						elif obj[4]<=0:
							# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[7]>0.0:
								return 'True'
							elif obj[7]<=0.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[9]>2.0:
						return 'True'
					else: return 'True'
				elif obj[5]>3:
					return 'True'
				else: return 'True'
			elif obj[8]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[6]<=1:
			# {"feature": "Education", "instances": 14, "metric_value": 0.8631, "depth": 3}
			if obj[5]>0:
				# {"feature": "Bar", "instances": 8, "metric_value": 1.0, "depth": 4}
				if obj[7]<=1.0:
					# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[1]>0:
						return 'False'
					elif obj[1]<=0:
						# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[2]<=0:
							return 'False'
						elif obj[2]>0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[7]>1.0:
					return 'True'
				else: return 'True'
			elif obj[5]<=0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]>1:
		# {"feature": "Coupon", "instances": 32, "metric_value": 0.896, "depth": 2}
		if obj[2]>0:
			# {"feature": "Age", "instances": 30, "metric_value": 0.8366, "depth": 3}
			if obj[4]>0:
				# {"feature": "Occupation", "instances": 26, "metric_value": 0.7063, "depth": 4}
				if obj[6]>5:
					# {"feature": "Education", "instances": 16, "metric_value": 0.896, "depth": 5}
					if obj[5]>1:
						# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.994, "depth": 6}
						if obj[8]>0.0:
							# {"feature": "Bar", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[7]>0.0:
								# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[11]>1:
										return 'False'
									elif obj[11]<=1:
										return 'True'
									else: return 'True'
								elif obj[1]>2:
									return 'True'
								else: return 'True'
							elif obj[7]<=0.0:
								return 'True'
							else: return 'True'
						elif obj[8]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[5]<=1:
						return 'True'
					else: return 'True'
				elif obj[6]<=5:
					return 'True'
				else: return 'True'
			elif obj[4]<=0:
				# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[5]<=2:
					return 'False'
				elif obj[5]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]<=0:
			return 'False'
		else: return 'False'
	else: return 'True'
