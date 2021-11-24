def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Coffeehouse", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[7]>1.0:
		# {"feature": "Education", "instances": 26, "metric_value": 0.7793, "depth": 2}
		if obj[4]<=3:
			# {"feature": "Occupation", "instances": 24, "metric_value": 0.65, "depth": 3}
			if obj[5]>6:
				# {"feature": "Age", "instances": 13, "metric_value": 0.8905, "depth": 4}
				if obj[3]<=4:
					# {"feature": "Bar", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[6]<=3.0:
						return 'True'
					elif obj[6]>3.0:
						return 'False'
					else: return 'False'
				elif obj[3]>4:
					# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[10]>1:
						return 'False'
					elif obj[10]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[5]<=6:
				return 'True'
			else: return 'True'
		elif obj[4]>3:
			return 'False'
		else: return 'False'
	elif obj[7]<=1.0:
		# {"feature": "Distance", "instances": 25, "metric_value": 0.971, "depth": 2}
		if obj[10]>1:
			# {"feature": "Time", "instances": 19, "metric_value": 0.998, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Occupation", "instances": 16, "metric_value": 0.9544, "depth": 4}
				if obj[5]<=6:
					# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[2]<=3:
						return 'True'
					elif obj[2]>3:
						# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3]<=2:
							return 'True'
						elif obj[3]>2:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[5]>6:
					# {"feature": "Age", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[3]>0:
						# {"feature": "Bar", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[6]<=0.0:
							# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[2]>1:
									return 'True'
								elif obj[2]<=1:
									return 'False'
								else: return 'False'
							elif obj[0]>1:
								return 'False'
							else: return 'False'
						elif obj[6]>0.0:
							return 'True'
						else: return 'True'
					elif obj[3]<=0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[1]>3:
				return 'False'
			else: return 'False'
		elif obj[10]<=1:
			return 'False'
		else: return 'False'
	else: return 'False'
