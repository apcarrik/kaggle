def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[2]<=3:
		# {"feature": "Distance", "instances": 20, "metric_value": 0.9928, "depth": 2}
		if obj[5]>1:
			# {"feature": "Occupation", "instances": 14, "metric_value": 0.9852, "depth": 3}
			if obj[3]>4:
				# {"feature": "Passanger", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Coupon", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[1]<=2:
						# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[4]>0.0:
							return 'True'
						elif obj[4]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[1]>2:
						return 'True'
					else: return 'True'
				elif obj[0]>2:
					return 'False'
				else: return 'False'
			elif obj[3]<=4:
				return 'False'
			else: return 'False'
		elif obj[5]<=1:
			# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[1]<=3:
				return 'True'
			elif obj[1]>3:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]<=0:
					return 'True'
				elif obj[0]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[2]>3:
		return 'True'
	else: return 'True'
