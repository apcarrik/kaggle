def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[5]<=2:
		# {"feature": "Coupon", "instances": 19, "metric_value": 0.8997, "depth": 2}
		if obj[1]>2:
			# {"feature": "Occupation", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[3]<=7:
				# {"feature": "Education", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[2]>0:
					# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[0]>1:
							return 'False'
						elif obj[0]<=1:
							return 'False'
						else: return 'False'
					elif obj[4]>1.0:
						return 'True'
					else: return 'True'
				elif obj[2]<=0:
					return 'True'
				else: return 'True'
			elif obj[3]>7:
				return 'False'
			else: return 'False'
		elif obj[1]<=2:
			return 'True'
		else: return 'True'
	elif obj[5]>2:
		return 'False'
	else: return 'False'
