def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[2]<=3:
		# {"feature": "Passanger", "instances": 31, "metric_value": 0.9992, "depth": 2}
		if obj[0]>0:
			# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.9991, "depth": 3}
			if obj[4]>0.0:
				# {"feature": "Distance", "instances": 23, "metric_value": 0.9877, "depth": 4}
				if obj[5]<=2:
					# {"feature": "Coupon", "instances": 18, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Occupation", "instances": 11, "metric_value": 0.994, "depth": 6}
						if obj[3]>2:
							return 'False'
						elif obj[3]<=2:
							return 'True'
						else: return 'True'
					elif obj[1]>3:
						# {"feature": "Occupation", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[3]>1:
							return 'True'
						elif obj[3]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[5]>2:
					# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[1]>1:
						# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[3]<=2:
							return 'False'
						elif obj[3]>2:
							return 'True'
						else: return 'True'
					elif obj[1]<=1:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[4]<=0.0:
				# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[3]<=2:
					# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[5]>1:
						# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]<=4:
							return 'True'
						else: return 'True'
					elif obj[5]<=1:
						return 'False'
					else: return 'False'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	elif obj[2]>3:
		return 'True'
	else: return 'True'
