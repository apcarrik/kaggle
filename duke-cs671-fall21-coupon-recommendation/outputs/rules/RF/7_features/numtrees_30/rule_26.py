def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Distance", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[6]<=2:
		# {"feature": "Coupon", "instances": 28, "metric_value": 0.8631, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.5226, "depth": 3}
			if obj[4]>1.0:
				return 'True'
			elif obj[4]<=1.0:
				# {"feature": "Education", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[2]<=1:
					# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[3]<=5:
						# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]>0:
								return 'True'
							elif obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					elif obj[3]>5:
						return 'False'
					else: return 'False'
				elif obj[2]>1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[1]>3:
			# {"feature": "Occupation", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[3]>7:
				# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[2]>0:
					return 'False'
				elif obj[2]<=0:
					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[5]>0:
						return 'False'
					elif obj[5]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[3]<=7:
				# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[0]>1:
					return 'True'
				elif obj[0]<=1:
					# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2]<=0:
						# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]<=2.0:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[6]>2:
		# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[3]>1:
			return 'False'
		elif obj[3]<=1:
			# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1]>1:
				return 'False'
			elif obj[1]<=1:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
