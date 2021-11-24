def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Distance", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[5]<=2:
		# {"feature": "Coupon", "instances": 44, "metric_value": 0.994, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Passanger", "instances": 28, "metric_value": 0.9403, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.7871, "depth": 4}
				if obj[4]>-1.0:
					# {"feature": "Education", "instances": 16, "metric_value": 0.6962, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Occupation", "instances": 12, "metric_value": 0.8113, "depth": 6}
						if obj[3]>1:
							return 'True'
						elif obj[3]<=1:
							return 'True'
						else: return 'True'
					elif obj[2]>2:
						return 'True'
					else: return 'True'
				elif obj[4]<=-1.0:
					return 'False'
				else: return 'False'
			elif obj[0]>1:
				# {"feature": "Education", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[4]>0.0:
						# {"feature": "Occupation", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[3]<=3:
							return 'False'
						elif obj[3]>3:
							return 'True'
						else: return 'True'
					elif obj[4]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[2]>3:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[1]>3:
			# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.9544, "depth": 3}
			if obj[4]<=1.0:
				# {"feature": "Occupation", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[3]<=5:
					# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[0]>1:
						# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]<=0:
							return 'True'
						elif obj[2]>0:
							return 'False'
						else: return 'False'
					elif obj[0]<=1:
						return 'False'
					else: return 'False'
				elif obj[3]>5:
					return 'True'
				else: return 'True'
			elif obj[4]>1.0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[5]>2:
		# {"feature": "Occupation", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[3]<=11:
			return 'False'
		elif obj[3]>11:
			return 'True'
		else: return 'True'
	else: return 'False'
