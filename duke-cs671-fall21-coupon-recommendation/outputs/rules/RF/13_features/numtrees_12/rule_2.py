def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Bar", "instances": 85, "metric_value": 0.9018, "depth": 1}
	if obj[8]>0.0:
		# {"feature": "Age", "instances": 50, "metric_value": 0.7602, "depth": 2}
		if obj[4]<=3:
			# {"feature": "Gender", "instances": 27, "metric_value": 0.9183, "depth": 3}
			if obj[3]<=0:
				# {"feature": "Children", "instances": 15, "metric_value": 0.7219, "depth": 4}
				if obj[5]<=0:
					# {"feature": "Occupation", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[7]>5:
						# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[1]>0:
							# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[9]<=0.0:
								# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[2]<=3:
									return 'True'
								elif obj[2]>3:
									return 'False'
								else: return 'False'
							elif obj[9]>0.0:
								return 'False'
							else: return 'False'
						elif obj[1]<=0:
							return 'True'
						else: return 'True'
					elif obj[7]<=5:
						return 'True'
					else: return 'True'
				elif obj[5]>0:
					return 'True'
				else: return 'True'
			elif obj[3]>0:
				# {"feature": "Education", "instances": 12, "metric_value": 1.0, "depth": 4}
				if obj[6]>0:
					# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[12]>1:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[0]>1:
							# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[7]<=6:
								return 'False'
							elif obj[7]>6:
								return 'True'
							else: return 'True'
						elif obj[0]<=1:
							return 'True'
						else: return 'True'
					elif obj[12]<=1:
						return 'False'
					else: return 'False'
				elif obj[6]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[4]>3:
			# {"feature": "Time", "instances": 23, "metric_value": 0.4262, "depth": 3}
			if obj[1]>2:
				return 'True'
			elif obj[1]<=2:
				# {"feature": "Occupation", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[7]>6:
					return 'True'
				elif obj[7]<=6:
					# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[6]<=1:
						return 'True'
					elif obj[6]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[8]<=0.0:
		# {"feature": "Coupon", "instances": 35, "metric_value": 0.9947, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Age", "instances": 19, "metric_value": 0.8997, "depth": 3}
			if obj[4]>0:
				# {"feature": "Occupation", "instances": 15, "metric_value": 0.7219, "depth": 4}
				if obj[7]>5:
					# {"feature": "Gender", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[3]>0:
						# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[0]>0:
							# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[1]>0:
								# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[9]<=3.0:
									return 'True'
								elif obj[9]>3.0:
									return 'False'
								else: return 'False'
							elif obj[1]<=0:
								return 'False'
							else: return 'False'
						elif obj[0]<=0:
							return 'False'
						else: return 'False'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				elif obj[7]<=5:
					return 'True'
				else: return 'True'
			elif obj[4]<=0:
				# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[0]<=1:
					return 'False'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]>3:
			# {"feature": "Age", "instances": 16, "metric_value": 0.9544, "depth": 3}
			if obj[4]>1:
				# {"feature": "Occupation", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[7]<=19:
					# {"feature": "Gender", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[3]>0:
						return 'False'
					elif obj[3]<=0:
						# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[9]<=0.0:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[1]<=1:
									# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[5]<=0:
										# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[6]<=0:
											# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[12]<=3:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[9]>0.0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[7]>19:
					return 'True'
				else: return 'True'
			elif obj[4]<=1:
				# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[7]>1:
					# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[9]<=2.0:
						return 'True'
					elif obj[9]>2.0:
						return 'False'
					else: return 'False'
				elif obj[7]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	else: return 'True'
