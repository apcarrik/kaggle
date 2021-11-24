def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9989, "depth": 1}
	if obj[2]>1:
		# {"feature": "Passanger", "instances": 78, "metric_value": 0.9418, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Distance", "instances": 52, "metric_value": 0.9957, "depth": 3}
			if obj[13]>1:
				# {"feature": "Age", "instances": 28, "metric_value": 0.9403, "depth": 4}
				if obj[4]<=5:
					# {"feature": "Income", "instances": 22, "metric_value": 0.994, "depth": 5}
					if obj[8]>2:
						# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.9183, "depth": 6}
						if obj[11]<=2.0:
							# {"feature": "Time", "instances": 16, "metric_value": 0.8113, "depth": 7}
							if obj[1]<=2:
								# {"feature": "Education", "instances": 11, "metric_value": 0.9457, "depth": 8}
								if obj[6]>1:
									# {"feature": "Children", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[5]<=0:
										return 'False'
									elif obj[5]>0:
										return 'True'
									else: return 'True'
								elif obj[6]<=1:
									# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[12]<=0:
											return 'True'
										elif obj[12]>0:
											# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[10]<=1.0:
												return 'False'
											elif obj[10]>1.0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[3]>0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[1]>2:
								return 'False'
							else: return 'False'
						elif obj[11]>2.0:
							return 'True'
						else: return 'True'
					elif obj[8]<=2:
						return 'True'
					else: return 'True'
				elif obj[4]>5:
					return 'False'
				else: return 'False'
			elif obj[13]<=1:
				# {"feature": "Education", "instances": 24, "metric_value": 0.8113, "depth": 4}
				if obj[6]<=2:
					# {"feature": "Time", "instances": 18, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=1:
						# {"feature": "Occupation", "instances": 10, "metric_value": 1.0, "depth": 6}
						if obj[7]>1:
							# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[11]<=1.0:
								return 'False'
							elif obj[11]>1.0:
								return 'True'
							else: return 'True'
						elif obj[7]<=1:
							return 'True'
						else: return 'True'
					elif obj[1]>1:
						# {"feature": "Occupation", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[7]>1:
							return 'True'
						elif obj[7]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[6]>2:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[0]>2:
			# {"feature": "Coffeehouse", "instances": 26, "metric_value": 0.6194, "depth": 3}
			if obj[10]>1.0:
				# {"feature": "Education", "instances": 14, "metric_value": 0.8631, "depth": 4}
				if obj[6]>1:
					# {"feature": "Distance", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[13]>1:
						# {"feature": "Age", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[4]>0:
							# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[3]>0:
								return 'True'
							elif obj[3]<=0:
								# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=1:
									return 'False'
								elif obj[7]>1:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[4]<=0:
							return 'False'
						else: return 'False'
					elif obj[13]<=1:
						return 'False'
					else: return 'False'
				elif obj[6]<=1:
					return 'True'
				else: return 'True'
			elif obj[10]<=1.0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Coffeehouse", "instances": 49, "metric_value": 0.9113, "depth": 2}
		if obj[10]<=1.0:
			# {"feature": "Passanger", "instances": 26, "metric_value": 0.7063, "depth": 3}
			if obj[0]>0:
				# {"feature": "Occupation", "instances": 18, "metric_value": 0.3095, "depth": 4}
				if obj[7]<=19:
					return 'False'
				elif obj[7]>19:
					return 'True'
				else: return 'True'
			elif obj[0]<=0:
				# {"feature": "Occupation", "instances": 8, "metric_value": 1.0, "depth": 4}
				if obj[7]<=4:
					# {"feature": "Bar", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[9]<=1.0:
						# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[1]>3:
							return 'True'
						elif obj[1]<=3:
							# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[11]>1.0:
								return 'False'
							elif obj[11]<=1.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[9]>1.0:
						return 'False'
					else: return 'False'
				elif obj[7]>4:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[10]>1.0:
			# {"feature": "Income", "instances": 23, "metric_value": 0.9986, "depth": 3}
			if obj[8]<=7:
				# {"feature": "Time", "instances": 19, "metric_value": 0.9819, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Children", "instances": 16, "metric_value": 1.0, "depth": 5}
					if obj[5]>0:
						# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[7]<=4:
							# {"feature": "Bar", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[9]<=1.0:
								return 'False'
							elif obj[9]>1.0:
								return 'True'
							else: return 'True'
						elif obj[7]>4:
							return 'True'
						else: return 'True'
					elif obj[5]<=0:
						# {"feature": "Bar", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[9]>0.0:
							return 'False'
						elif obj[9]<=0.0:
							# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[13]<=2:
								return 'True'
							elif obj[13]>2:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				elif obj[1]>3:
					return 'True'
				else: return 'True'
			elif obj[8]>7:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'
