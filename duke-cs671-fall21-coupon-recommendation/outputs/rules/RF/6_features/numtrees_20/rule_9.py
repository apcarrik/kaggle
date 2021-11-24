def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[3]<=14:
		# {"feature": "Passanger", "instances": 46, "metric_value": 1.0, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Coupon", "instances": 26, "metric_value": 0.9612, "depth": 3}
			if obj[1]>0:
				# {"feature": "Education", "instances": 22, "metric_value": 0.994, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Distance", "instances": 20, "metric_value": 0.971, "depth": 5}
					if obj[5]<=2:
						# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.896, "depth": 6}
						if obj[4]<=3.0:
							return 'False'
						elif obj[4]>3.0:
							return 'True'
						else: return 'True'
					elif obj[5]>2:
						# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[4]>1.0:
							return 'False'
						elif obj[4]<=1.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[2]>3:
					return 'True'
				else: return 'True'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		elif obj[0]>1:
			# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 0.9341, "depth": 3}
			if obj[4]>0.0:
				# {"feature": "Coupon", "instances": 18, "metric_value": 0.8524, "depth": 4}
				if obj[1]>1:
					# {"feature": "Education", "instances": 12, "metric_value": 0.65, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Distance", "instances": 10, "metric_value": 0.469, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					elif obj[2]>3:
						# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]<=1:
							return 'True'
						elif obj[5]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[1]<=1:
					# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[2]>0:
						# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[5]>1:
							return 'False'
						elif obj[5]<=1:
							return 'False'
						else: return 'False'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[4]<=0.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[3]>14:
		return 'True'
	else: return 'True'
