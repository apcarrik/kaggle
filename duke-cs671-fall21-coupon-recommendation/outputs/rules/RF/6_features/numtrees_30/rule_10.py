def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[4]<=2.0:
		# {"feature": "Passanger", "instances": 32, "metric_value": 0.9972, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Coupon", "instances": 24, "metric_value": 0.995, "depth": 3}
			if obj[1]>1:
				# {"feature": "Occupation", "instances": 16, "metric_value": 0.896, "depth": 4}
				if obj[3]<=13:
					# {"feature": "Education", "instances": 13, "metric_value": 0.9612, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Distance", "instances": 12, "metric_value": 0.9799, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					elif obj[2]>3:
						return 'True'
					else: return 'True'
				elif obj[3]>13:
					return 'True'
				else: return 'True'
			elif obj[1]<=1:
				# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[3]>1:
					# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[2]>0:
						return 'False'
					elif obj[2]<=0:
						# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[0]>2:
			# {"feature": "Education", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[2]>0:
				return 'False'
			elif obj[2]<=0:
				# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]>7:
					return 'True'
				elif obj[3]<=7:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[4]>2.0:
		return 'True'
	else: return 'True'
