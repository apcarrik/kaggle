def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[1]>0:
		# {"feature": "Passanger", "instances": 47, "metric_value": 0.9252, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Distance", "instances": 32, "metric_value": 0.9887, "depth": 3}
			if obj[5]<=1:
				# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.8524, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "Occupation", "instances": 17, "metric_value": 0.7871, "depth": 5}
					if obj[3]>3:
						# {"feature": "Education", "instances": 12, "metric_value": 0.9183, "depth": 6}
						if obj[2]>0:
							return 'True'
						elif obj[2]<=0:
							return 'True'
						else: return 'True'
					elif obj[3]<=3:
						return 'True'
					else: return 'True'
				elif obj[4]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[5]>1:
				# {"feature": "Occupation", "instances": 14, "metric_value": 0.9403, "depth": 4}
				if obj[3]<=7:
					# {"feature": "Education", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[2]>0:
						# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[4]<=2.0:
							return 'False'
						elif obj[4]>2.0:
							return 'True'
						else: return 'True'
					elif obj[2]<=0:
						# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[4]>0.0:
							return 'True'
						elif obj[4]<=0.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[3]>7:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[0]>1:
			# {"feature": "Education", "instances": 15, "metric_value": 0.5665, "depth": 3}
			if obj[2]>0:
				# {"feature": "Occupation", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[3]>4:
					# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[5]<=1:
						# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[4]<=1.0:
							return 'True'
						elif obj[4]>1.0:
							return 'True'
						else: return 'True'
					elif obj[5]>1:
						# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]<=2.0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[3]<=4:
					return 'True'
				else: return 'True'
			elif obj[2]<=0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[1]<=0:
		return 'False'
	else: return 'False'
