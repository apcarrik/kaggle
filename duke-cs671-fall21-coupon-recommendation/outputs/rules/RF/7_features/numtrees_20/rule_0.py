def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[1]>0:
		# {"feature": "Occupation", "instances": 41, "metric_value": 0.9262, "depth": 2}
		if obj[3]<=10:
			# {"feature": "Restaurant20to50", "instances": 26, "metric_value": 0.7793, "depth": 3}
			if obj[4]>0.0:
				# {"feature": "Education", "instances": 21, "metric_value": 0.8631, "depth": 4}
				if obj[2]>0:
					# {"feature": "Direction_same", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[5]<=0:
						# {"feature": "Passanger", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[0]>0:
							# {"feature": "Distance", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[6]<=1:
								return 'True'
							elif obj[6]>1:
								return 'True'
							else: return 'True'
						elif obj[0]<=0:
							return 'False'
						else: return 'False'
					elif obj[5]>0:
						return 'False'
					else: return 'False'
				elif obj[2]<=0:
					# {"feature": "Passanger", "instances": 10, "metric_value": 0.469, "depth": 5}
					if obj[0]<=2:
						return 'True'
					elif obj[0]>2:
						# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[6]>1:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[6]<=1:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[4]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[3]>10:
			# {"feature": "Passanger", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[0]>0:
				# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 1.0, "depth": 4}
				if obj[4]<=1.0:
					# {"feature": "Distance", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[6]<=2:
						# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[2]>1:
							# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[2]<=1:
							return 'False'
						else: return 'False'
					elif obj[6]>2:
						# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[2]<=2:
							return 'True'
						elif obj[2]>2:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[4]>1.0:
					# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[2]>0:
						return 'False'
					elif obj[2]<=0:
						# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]>0:
							return 'False'
						elif obj[5]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'False'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[1]<=0:
		# {"feature": "Passanger", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[0]<=1:
			return 'False'
		elif obj[0]>1:
			# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[2]>0:
				return 'False'
			elif obj[2]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
