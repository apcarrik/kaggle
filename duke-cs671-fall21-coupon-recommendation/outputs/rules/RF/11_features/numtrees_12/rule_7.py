def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9999, "depth": 1}
	if obj[2]>1:
		# {"feature": "Education", "instances": 57, "metric_value": 0.9495, "depth": 2}
		if obj[4]<=3:
			# {"feature": "Time", "instances": 51, "metric_value": 0.9774, "depth": 3}
			if obj[1]>0:
				# {"feature": "Restaurant20to50", "instances": 40, "metric_value": 0.9097, "depth": 4}
				if obj[8]<=1.0:
					# {"feature": "Age", "instances": 21, "metric_value": 0.9984, "depth": 5}
					if obj[3]>0:
						# {"feature": "Occupation", "instances": 18, "metric_value": 0.9911, "depth": 6}
						if obj[5]<=19:
							# {"feature": "Bar", "instances": 16, "metric_value": 0.9544, "depth": 7}
							if obj[6]<=1.0:
								# {"feature": "Coffeehouse", "instances": 12, "metric_value": 1.0, "depth": 8}
								if obj[7]<=1.0:
									# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 9}
									if obj[10]>1:
										# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[0]>1:
											return 'False'
										else: return 'False'
									elif obj[10]<=1:
										return 'False'
									else: return 'False'
								elif obj[7]>1.0:
									# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[10]>1:
										# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[0]>1:
											return 'True'
										else: return 'True'
									elif obj[10]<=1:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[6]>1.0:
								return 'False'
							else: return 'False'
						elif obj[5]>19:
							return 'True'
						else: return 'True'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				elif obj[8]>1.0:
					# {"feature": "Passanger", "instances": 19, "metric_value": 0.6292, "depth": 5}
					if obj[0]>0:
						# {"feature": "Occupation", "instances": 17, "metric_value": 0.3228, "depth": 6}
						if obj[5]<=18:
							return 'True'
						elif obj[5]>18:
							return 'False'
						else: return 'False'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[1]<=0:
				# {"feature": "Occupation", "instances": 11, "metric_value": 0.8454, "depth": 4}
				if obj[5]<=6:
					return 'False'
				elif obj[5]>6:
					# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[7]<=2.0:
						return 'True'
					elif obj[7]>2.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[4]>3:
			return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Bar", "instances": 28, "metric_value": 0.8113, "depth": 2}
		if obj[6]>0.0:
			# {"feature": "Occupation", "instances": 14, "metric_value": 1.0, "depth": 3}
			if obj[5]<=5:
				# {"feature": "Age", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[3]<=1:
					return 'True'
				elif obj[3]>1:
					# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[1]>0:
						# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]>0:
							return 'True'
						elif obj[4]<=0:
							return 'False'
						else: return 'False'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[5]>5:
				# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[7]<=1.0:
					return 'False'
				elif obj[7]>1.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[6]<=0.0:
			return 'False'
		else: return 'False'
	else: return 'False'
