def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.8338, "depth": 1}
	if obj[3]>5:
		# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 0.9928, "depth": 2}
		if obj[4]<=1.0:
			# {"feature": "Passanger", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Education", "instances": 13, "metric_value": 0.9957, "depth": 4}
				if obj[2]<=2:
					# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[6]<=2:
						# {"feature": "Coupon", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[1]<=0:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[1]>0:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=1:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[6]>2:
						return 'False'
					else: return 'False'
				elif obj[2]>2:
					# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=2:
						# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]>1:
								return 'True'
							elif obj[6]<=1:
								return 'True'
							else: return 'True'
						elif obj[5]>0:
							# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]<=1:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[1]>2:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[0]>2:
				return 'False'
			else: return 'False'
		elif obj[4]>1.0:
			# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]<=1:
							# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]<=2:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[2]>3:
					return 'True'
				else: return 'True'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[3]<=5:
		return 'True'
	else: return 'True'
