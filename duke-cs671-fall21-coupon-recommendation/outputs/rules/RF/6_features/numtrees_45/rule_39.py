def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[5]>1:
		# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9957, "depth": 2}
		if obj[4]>0.0:
			# {"feature": "Passanger", "instances": 11, "metric_value": 0.9457, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Coupon", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[1]>0:
					# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[3]>5:
							return 'False'
						elif obj[3]<=5:
							return 'True'
						else: return 'True'
					elif obj[2]>2:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			elif obj[0]>2:
				return 'False'
			else: return 'False'
		elif obj[4]<=0.0:
			return 'True'
		else: return 'True'
	elif obj[5]<=1:
		# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[3]>4:
			return 'True'
		elif obj[3]<=4:
			# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]<=1.0:
							return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'True'
