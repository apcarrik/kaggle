def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9999, "depth": 1}
	if obj[2]>1:
		# {"feature": "Occupation", "instances": 59, "metric_value": 0.9748, "depth": 2}
		if obj[6]<=10:
			# {"feature": "Education", "instances": 40, "metric_value": 0.8813, "depth": 3}
			if obj[5]<=3:
				# {"feature": "Bar", "instances": 36, "metric_value": 0.9183, "depth": 4}
				if obj[7]<=2.0:
					# {"feature": "Passanger", "instances": 33, "metric_value": 0.9457, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Time", "instances": 23, "metric_value": 0.8281, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Gender", "instances": 14, "metric_value": 0.9852, "depth": 7}
							if obj[3]>0:
								# {"feature": "Age", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[4]>0:
									# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[8]>0.0:
										return 'True'
									elif obj[8]<=0.0:
										return 'False'
									else: return 'False'
								elif obj[4]<=0:
									return 'False'
								else: return 'False'
							elif obj[3]<=0:
								# {"feature": "Age", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[4]<=1:
									# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[8]>0.0:
										# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[9]>1.0:
											return 'True'
										elif obj[9]<=1.0:
											return 'False'
										else: return 'False'
									elif obj[8]<=0.0:
										return 'True'
									else: return 'True'
								elif obj[4]>1:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[1]>1:
							return 'True'
						else: return 'True'
					elif obj[0]>2:
						# {"feature": "Time", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[1]<=2:
							# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[9]>1.0:
								# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[4]>3:
									return 'False'
								elif obj[4]<=3:
									return 'True'
								else: return 'True'
							elif obj[9]<=1.0:
								return 'True'
							else: return 'True'
						elif obj[1]>2:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[7]>2.0:
					return 'True'
				else: return 'True'
			elif obj[5]>3:
				return 'True'
			else: return 'True'
		elif obj[6]>10:
			# {"feature": "Bar", "instances": 19, "metric_value": 0.9495, "depth": 3}
			if obj[7]<=2.0:
				# {"feature": "Passanger", "instances": 15, "metric_value": 0.9968, "depth": 4}
				if obj[0]>0:
					# {"feature": "Education", "instances": 13, "metric_value": 0.9957, "depth": 5}
					if obj[5]>0:
						# {"feature": "Direction_same", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[10]<=0:
							# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[1]>0:
								# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[8]>0.0:
									# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[4]>0:
										return 'False'
									elif obj[4]<=0:
										# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[11]<=1:
											return 'True'
										elif obj[11]>1:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[8]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[1]<=0:
								return 'False'
							else: return 'False'
						elif obj[10]>0:
							return 'True'
						else: return 'True'
					elif obj[5]<=0:
						return 'True'
					else: return 'True'
				elif obj[0]<=0:
					return 'False'
				else: return 'False'
			elif obj[7]>2.0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[2]<=1:
		# {"feature": "Passanger", "instances": 26, "metric_value": 0.8404, "depth": 2}
		if obj[0]>0:
			# {"feature": "Education", "instances": 23, "metric_value": 0.6666, "depth": 3}
			if obj[5]<=3:
				# {"feature": "Bar", "instances": 21, "metric_value": 0.4537, "depth": 4}
				if obj[7]>1.0:
					# {"feature": "Time", "instances": 12, "metric_value": 0.65, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Occupation", "instances": 11, "metric_value": 0.4395, "depth": 6}
						if obj[6]>5:
							return 'False'
						elif obj[6]<=5:
							# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4]<=0:
								return 'True'
							elif obj[4]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				elif obj[7]<=1.0:
					return 'False'
				else: return 'False'
			elif obj[5]>3:
				return 'True'
			else: return 'True'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
