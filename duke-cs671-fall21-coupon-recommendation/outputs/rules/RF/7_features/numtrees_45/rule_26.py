def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[6]>1:
		# {"feature": "Occupation", "instances": 18, "metric_value": 0.9183, "depth": 2}
		if obj[3]<=7:
			# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[4]>0.0:
				# {"feature": "Education", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[2]>1:
					# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[1]<=3:
							# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[1]>3:
							return 'False'
						else: return 'False'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				elif obj[2]<=1:
					return 'True'
				else: return 'True'
			elif obj[4]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[3]>7:
			return 'False'
		else: return 'False'
	elif obj[6]<=1:
		return 'True'
	else: return 'True'
