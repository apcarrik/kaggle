def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[3]<=2:
		# {"feature": "Time", "instances": 19, "metric_value": 0.9819, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Passanger", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[4]<=7:
					return 'False'
				elif obj[4]>7:
					# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=2:
						return 'True'
					elif obj[2]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[0]>1:
				# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[4]<=10:
					return 'True'
				elif obj[4]>10:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[1]>2:
			# {"feature": "Occupation", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[4]<=7:
				return 'True'
			elif obj[4]>7:
				# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[5]>0.0:
					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[6]<=0.0:
						return 'True'
					elif obj[6]>0.0:
						return 'False'
					else: return 'False'
				elif obj[5]<=0.0:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[3]>2:
		return 'False'
	else: return 'False'
