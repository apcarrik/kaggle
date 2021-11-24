def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[3]<=8.07843137254902:
		# {"feature": "Coupon", "instances": 31, "metric_value": 0.8238, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Distance", "instances": 23, "metric_value": 0.5586, "depth": 3}
			if obj[6]<=2:
				# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.4395, "depth": 4}
				if obj[4]<=1.0:
					# {"feature": "Education", "instances": 12, "metric_value": 0.65, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Direction_same", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[0]>2:
							return 'False'
						else: return 'False'
					elif obj[2]>2:
						return 'True'
					else: return 'True'
				elif obj[4]>1.0:
					return 'True'
				else: return 'True'
			elif obj[6]>2:
				return 'False'
			else: return 'False'
		elif obj[1]>3:
			# {"feature": "Passanger", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[4]<=2.0:
					return 'False'
				elif obj[4]>2.0:
					return 'True'
				else: return 'True'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[3]>8.07843137254902:
		# {"feature": "Education", "instances": 20, "metric_value": 0.8113, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Coupon", "instances": 19, "metric_value": 0.7425, "depth": 3}
			if obj[1]>1:
				# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.8366, "depth": 4}
				if obj[4]<=2.0:
					# {"feature": "Passanger", "instances": 13, "metric_value": 0.8905, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Distance", "instances": 11, "metric_value": 0.8454, "depth": 6}
						if obj[6]<=1:
							# {"feature": "Direction_same", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[5]>0:
								return 'False'
							elif obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[6]>1:
							# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[0]>2:
						# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[6]>1:
							return 'False'
						elif obj[6]<=1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[4]>2.0:
					return 'False'
				else: return 'False'
			elif obj[1]<=1:
				return 'False'
			else: return 'False'
		elif obj[2]>3:
			return 'True'
		else: return 'True'
	else: return 'False'
