def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Restaurant20to50", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[4]<=2.0:
		# {"feature": "Occupation", "instances": 47, "metric_value": 0.9971, "depth": 2}
		if obj[3]<=7:
			# {"feature": "Coupon", "instances": 30, "metric_value": 0.971, "depth": 3}
			if obj[1]>1:
				# {"feature": "Distance", "instances": 21, "metric_value": 0.8631, "depth": 4}
				if obj[5]<=1:
					# {"feature": "Passanger", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[0]>0:
						# {"feature": "Education", "instances": 11, "metric_value": 0.9457, "depth": 6}
						if obj[2]>0:
							return 'True'
						elif obj[2]<=0:
							return 'False'
						else: return 'False'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				elif obj[5]>1:
					# {"feature": "Education", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[2]>0:
						return 'True'
					elif obj[2]<=0:
						# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[0]<=1:
							return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[1]<=1:
				# {"feature": "Passanger", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Distance", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[5]<=2:
						# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[2]>0:
							return 'False'
						elif obj[2]<=0:
							return 'False'
						else: return 'False'
					elif obj[5]>2:
						return 'False'
					else: return 'False'
				elif obj[0]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[3]>7:
			# {"feature": "Distance", "instances": 17, "metric_value": 0.7871, "depth": 3}
			if obj[5]>1:
				# {"feature": "Coupon", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[1]>0:
					# {"feature": "Education", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[0]>0:
							return 'False'
						elif obj[0]<=0:
							return 'False'
						else: return 'False'
					elif obj[2]>2:
						# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[0]>1:
							return 'True'
						elif obj[0]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			elif obj[5]<=1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[4]>2.0:
		return 'True'
	else: return 'True'
