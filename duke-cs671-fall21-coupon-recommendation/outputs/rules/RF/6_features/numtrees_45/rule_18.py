def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[1]>1:
		# {"feature": "Education", "instances": 17, "metric_value": 0.9367, "depth": 2}
		if obj[2]<=2:
			# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[4]<=1.0:
				# {"feature": "Occupation", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[3]<=13:
					# {"feature": "Passanger", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[0]>1:
						# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[5]>1:
							return 'False'
						elif obj[5]<=1:
							return 'False'
						else: return 'False'
					elif obj[0]<=1:
						# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[5]<=1:
							return 'False'
						elif obj[5]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[3]>13:
					return 'True'
				else: return 'True'
			elif obj[4]>1.0:
				return 'True'
			else: return 'True'
		elif obj[2]>2:
			return 'True'
		else: return 'True'
	elif obj[1]<=1:
		# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[2]>0:
			return 'False'
		elif obj[2]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
