def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[4]>2:
		# {"feature": "Coupon", "instances": 16, "metric_value": 0.896, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Bar", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[5]>0.0:
				# {"feature": "Time", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[1]>0:
					# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[6]<=1.0:
						# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[8]<=1:
							return 'True'
						elif obj[8]>1:
							return 'False'
						else: return 'False'
					elif obj[6]>1.0:
						return 'True'
					else: return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			elif obj[5]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[2]>3:
			return 'False'
		else: return 'False'
	elif obj[4]<=2:
		# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[2]>0:
			return 'True'
		elif obj[2]<=0:
			return 'False'
		else: return 'False'
	else: return 'True'
