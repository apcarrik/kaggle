def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9526, "depth": 1}
	if obj[3]<=9:
		# {"feature": "Coupon", "instances": 33, "metric_value": 0.8454, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Bar", "instances": 28, "metric_value": 0.7496, "depth": 3}
			if obj[4]<=2.0:
				# {"feature": "Restaurant20to50", "instances": 24, "metric_value": 0.8113, "depth": 4}
				if obj[5]<=2.0:
					# {"feature": "Education", "instances": 20, "metric_value": 0.8813, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Passanger", "instances": 17, "metric_value": 0.7871, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Distance", "instances": 9, "metric_value": 0.5033, "depth": 7}
							if obj[7]<=1:
								return 'True'
							elif obj[7]>1:
								# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[0]>1:
							# {"feature": "Direction_same", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[7]>1:
									return 'True'
								elif obj[7]<=1:
									return 'True'
								else: return 'True'
							elif obj[6]>0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[2]>2:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=0:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=2:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[0]>0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[5]>2.0:
					return 'True'
				else: return 'True'
			elif obj[4]>2.0:
				return 'True'
			else: return 'True'
		elif obj[1]>3:
			# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[0]>1:
				# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[2]>0:
					# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]>0.0:
						return 'False'
					elif obj[4]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[2]<=0:
					return 'True'
				else: return 'True'
			elif obj[0]<=1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[3]>9:
		# {"feature": "Coupon", "instances": 18, "metric_value": 0.9911, "depth": 2}
		if obj[1]>0:
			# {"feature": "Bar", "instances": 16, "metric_value": 1.0, "depth": 3}
			if obj[4]>0.0:
				# {"feature": "Passanger", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[0]>0:
					# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[5]<=2.0:
						# {"feature": "Distance", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[7]>1:
							# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[2]>0:
								# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[2]<=0:
								return 'True'
							else: return 'True'
						elif obj[7]<=1:
							return 'True'
						else: return 'True'
					elif obj[5]>2.0:
						return 'False'
					else: return 'False'
				elif obj[0]<=0:
					return 'False'
				else: return 'False'
			elif obj[4]<=0.0:
				# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[0]<=2:
					return 'False'
				elif obj[0]>2:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=0:
						# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]<=1.0:
							return 'False'
						elif obj[5]>1.0:
							return 'True'
						else: return 'True'
					elif obj[2]>0:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[1]<=0:
			return 'False'
		else: return 'False'
	else: return 'False'
