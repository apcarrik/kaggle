def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[4]<=12:
		# {"feature": "Time", "instances": 19, "metric_value": 0.9819, "depth": 2}
		if obj[1]>1:
			# {"feature": "Distance", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[8]>1:
				# {"feature": "Passanger", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[0]<=2:
					return 'False'
				elif obj[0]>2:
					# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[2]<=3:
						return 'True'
					elif obj[2]>3:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[8]<=1:
				# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[0]>1:
					# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[5]<=0.0:
						return 'False'
					elif obj[5]>0.0:
						return 'True'
					else: return 'True'
				elif obj[0]<=1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[1]<=1:
			return 'True'
		else: return 'True'
	elif obj[4]>12:
		return 'False'
	else: return 'False'
