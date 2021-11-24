def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Occupation", "instances": 20, "metric_value": 1.0, "depth": 2}
		if obj[3]<=6:
			# {"feature": "Coupon", "instances": 11, "metric_value": 0.9457, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[2]<=3:
					return 'True'
				elif obj[2]>3:
					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]>1.0:
						return 'False'
					elif obj[4]<=1.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[1]>2:
				# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[2]>0:
					return 'False'
				elif obj[2]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[3]>6:
			# {"feature": "Coupon", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[1]>1:
				# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[6]<=1:
					# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[5]>0:
						return 'True'
					elif obj[5]<=0:
						# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[2]>0:
							return 'True'
						elif obj[2]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[6]>1:
					return 'False'
				else: return 'False'
			elif obj[1]<=1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]>2:
		return 'True'
	else: return 'True'
