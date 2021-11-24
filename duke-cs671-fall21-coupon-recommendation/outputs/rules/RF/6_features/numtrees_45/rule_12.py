def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Distance", "instances": 17, "metric_value": 0.9975, "depth": 2}
		if obj[5]<=2:
			# {"feature": "Occupation", "instances": 14, "metric_value": 0.9852, "depth": 3}
			if obj[3]>5:
				# {"feature": "Coupon", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[2]>0:
						# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[4]>1.0:
							return 'True'
						elif obj[4]<=1.0:
							return 'False'
						else: return 'False'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				elif obj[1]>3:
					return 'False'
				else: return 'False'
			elif obj[3]<=5:
				return 'True'
			else: return 'True'
		elif obj[5]>2:
			return 'False'
		else: return 'False'
	elif obj[0]>2:
		return 'True'
	else: return 'True'
