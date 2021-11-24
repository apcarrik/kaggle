def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[2]<=3:
		# {"feature": "Coffeehouse", "instances": 31, "metric_value": 0.9072, "depth": 2}
		if obj[6]>1.0:
			# {"feature": "Direction_same", "instances": 19, "metric_value": 0.998, "depth": 3}
			if obj[8]<=0:
				# {"feature": "Passanger", "instances": 16, "metric_value": 0.9887, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Education", "instances": 11, "metric_value": 0.8454, "depth": 5}
					if obj[3]>0:
						return 'False'
					elif obj[3]<=0:
						# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[1]>2:
							# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[9]<=1:
								return 'False'
							elif obj[9]>1:
								return 'True'
							else: return 'True'
						elif obj[1]<=2:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[0]>2:
					# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[4]>2:
						return 'True'
					elif obj[4]<=2:
						# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]<=0:
							return 'True'
						elif obj[1]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			elif obj[8]>0:
				return 'True'
			else: return 'True'
		elif obj[6]<=1.0:
			# {"feature": "Time", "instances": 12, "metric_value": 0.4138, "depth": 3}
			if obj[1]<=3:
				return 'True'
			elif obj[1]>3:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[2]>3:
		# {"feature": "Bar", "instances": 20, "metric_value": 0.971, "depth": 2}
		if obj[5]<=0.0:
			# {"feature": "Passanger", "instances": 13, "metric_value": 0.7793, "depth": 3}
			if obj[0]<=2:
				return 'False'
			elif obj[0]>2:
				# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[3]<=2:
					# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4]<=8:
						return 'False'
					elif obj[4]>8:
						return 'True'
					else: return 'True'
				elif obj[3]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[5]>0.0:
			# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[7]<=1.0:
				# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[0]<=2:
					return 'True'
				elif obj[0]>2:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]<=2:
						return 'True'
					elif obj[1]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[7]>1.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
