def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Passanger", "instances": 85, "metric_value": 0.9991, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Occupation", "instances": 57, "metric_value": 0.9495, "depth": 2}
		if obj[3]<=12:
			# {"feature": "Coupon", "instances": 49, "metric_value": 0.9852, "depth": 3}
			if obj[1]>0:
				# {"feature": "Education", "instances": 38, "metric_value": 1.0, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Restaurant20to50", "instances": 37, "metric_value": 0.9995, "depth": 5}
					if obj[4]>-1.0:
						# {"feature": "Distance", "instances": 36, "metric_value": 1.0, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'False'
						else: return 'False'
					elif obj[4]<=-1.0:
						return 'True'
					else: return 'True'
				elif obj[2]>3:
					return 'False'
				else: return 'False'
			elif obj[1]<=0:
				# {"feature": "Education", "instances": 11, "metric_value": 0.684, "depth": 4}
				if obj[2]<=2:
					# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[4]>0.0:
						# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[5]<=1:
							return 'False'
						elif obj[5]>1:
							return 'False'
						else: return 'False'
					elif obj[4]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[2]>2:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[3]>12:
			return 'False'
		else: return 'False'
	elif obj[0]>2:
		# {"feature": "Coupon", "instances": 28, "metric_value": 0.8631, "depth": 2}
		if obj[1]>1:
			# {"feature": "Education", "instances": 24, "metric_value": 0.7383, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Occupation", "instances": 23, "metric_value": 0.6666, "depth": 4}
				if obj[3]<=12:
					# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.7425, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Distance", "instances": 17, "metric_value": 0.7871, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					elif obj[4]>1.0:
						return 'True'
					else: return 'True'
				elif obj[3]>12:
					return 'True'
				else: return 'True'
			elif obj[2]>3:
				return 'False'
			else: return 'False'
		elif obj[1]<=1:
			# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[2]>0:
				# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3]<=1:
					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]<=2:
							return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'True'
