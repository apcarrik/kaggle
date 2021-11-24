def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[3]<=9:
		# {"feature": "Coupon", "instances": 37, "metric_value": 0.8419, "depth": 2}
		if obj[1]>1:
			# {"feature": "Education", "instances": 28, "metric_value": 0.6769, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Bar", "instances": 27, "metric_value": 0.6052, "depth": 4}
				if obj[4]<=0.0:
					# {"feature": "Distance", "instances": 15, "metric_value": 0.3534, "depth": 5}
					if obj[7]>1:
						return 'True'
					elif obj[7]<=1:
						# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[5]>0.0:
							# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[5]<=0.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]>0.0:
					# {"feature": "Passanger", "instances": 12, "metric_value": 0.8113, "depth": 5}
					if obj[0]>1:
						# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[5]<=1.0:
							return 'True'
						elif obj[5]>1.0:
							# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[7]<=1:
								return 'True'
							elif obj[7]>1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[0]<=1:
						# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[5]>0.0:
							# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=1:
									return 'True'
								elif obj[7]>1:
									return 'False'
								else: return 'False'
							elif obj[6]>0:
								# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]>1:
									return 'True'
								elif obj[7]<=1:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[5]<=0.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[2]>3:
				return 'False'
			else: return 'False'
		elif obj[1]<=1:
			# {"feature": "Bar", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[4]>0.0:
				# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[2]>0:
					return 'True'
				elif obj[2]<=0:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]>0:
						return 'False'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]<=0.0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[3]>9:
		# {"feature": "Bar", "instances": 14, "metric_value": 0.8631, "depth": 2}
		if obj[4]<=1.0:
			return 'False'
		elif obj[4]>1.0:
			return 'True'
		else: return 'True'
	else: return 'False'
