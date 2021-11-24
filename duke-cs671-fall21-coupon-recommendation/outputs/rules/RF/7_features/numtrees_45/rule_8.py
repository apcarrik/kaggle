def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.9641, "depth": 2}
		if obj[4]<=2.0:
			# {"feature": "Occupation", "instances": 16, "metric_value": 0.9887, "depth": 3}
			if obj[3]>5:
				# {"feature": "Coupon", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[1]>0:
					# {"feature": "Distance", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[6]>1:
						# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[2]<=2:
							return 'True'
						elif obj[2]>2:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[6]<=1:
						# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[2]<=0:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=1:
								return 'False'
							else: return 'False'
						elif obj[2]>0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			elif obj[3]<=5:
				# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[1]<=2:
					return 'True'
				elif obj[1]>2:
					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[5]<=0:
						return 'True'
					elif obj[5]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[4]>2.0:
			return 'True'
		else: return 'True'
	elif obj[0]>2:
		return 'True'
	else: return 'True'
