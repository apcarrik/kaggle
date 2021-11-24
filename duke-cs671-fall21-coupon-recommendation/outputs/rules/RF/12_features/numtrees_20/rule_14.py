def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[2]>1:
		# {"feature": "Distance", "instances": 42, "metric_value": 0.8926, "depth": 2}
		if obj[11]<=2:
			# {"feature": "Coffeehouse", "instances": 35, "metric_value": 0.9518, "depth": 3}
			if obj[8]<=2.0:
				# {"feature": "Occupation", "instances": 30, "metric_value": 0.9871, "depth": 4}
				if obj[6]>2:
					# {"feature": "Passanger", "instances": 19, "metric_value": 0.9819, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Age", "instances": 14, "metric_value": 0.8631, "depth": 6}
						if obj[4]>0:
							# {"feature": "Direction_same", "instances": 13, "metric_value": 0.7793, "depth": 7}
							if obj[10]<=0:
								# {"feature": "Bar", "instances": 12, "metric_value": 0.65, "depth": 8}
								if obj[7]<=1.0:
									return 'False'
								elif obj[7]>1.0:
									# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[1]>0:
											# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[9]<=1.0:
												return 'False'
											elif obj[9]>1.0:
												return 'True'
											else: return 'True'
										elif obj[1]<=0:
											return 'False'
										else: return 'False'
									elif obj[3]>0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[10]>0:
								return 'True'
							else: return 'True'
						elif obj[4]<=0:
							return 'True'
						else: return 'True'
					elif obj[0]>1:
						# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[4]>1:
							return 'True'
						elif obj[4]<=1:
							# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]<=2:
								return 'False'
							elif obj[1]>2:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[6]<=2:
					# {"feature": "Age", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[4]<=2:
						return 'True'
					elif obj[4]>2:
						# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[3]>0:
							# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[5]>0:
								return 'True'
							elif obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[3]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			elif obj[8]>2.0:
				return 'True'
			else: return 'True'
		elif obj[11]>2:
			return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Bar", "instances": 9, "metric_value": 0.7642, "depth": 2}
		if obj[7]<=1.0:
			return 'False'
		elif obj[7]>1.0:
			return 'True'
		else: return 'True'
	else: return 'False'
