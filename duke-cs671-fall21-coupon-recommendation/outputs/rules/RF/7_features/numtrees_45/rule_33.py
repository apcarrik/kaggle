def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[4]<=1.0:
		# {"feature": "Coupon", "instances": 18, "metric_value": 0.9911, "depth": 2}
		if obj[1]>1:
			# {"feature": "Occupation", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[3]<=19:
				# {"feature": "Education", "instances": 13, "metric_value": 0.9957, "depth": 4}
				if obj[2]<=2:
					# {"feature": "Passanger", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[0]>0:
						# {"feature": "Direction_same", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[6]<=1:
								return 'True'
							elif obj[6]>1:
								return 'True'
							else: return 'True'
						elif obj[5]>0:
							# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]>1:
								return 'False'
							elif obj[6]<=1:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				elif obj[2]>2:
					return 'False'
				else: return 'False'
			elif obj[3]>19:
				return 'True'
			else: return 'True'
		elif obj[1]<=1:
			return 'False'
		else: return 'False'
	elif obj[4]>1.0:
		return 'True'
	else: return 'True'
