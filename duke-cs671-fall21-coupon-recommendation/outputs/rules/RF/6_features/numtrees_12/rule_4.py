def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Passanger", "instances": 85, "metric_value": 0.9637, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Occupation", "instances": 51, "metric_value": 0.9931, "depth": 2}
		if obj[3]<=20:
			# {"feature": "Coupon", "instances": 47, "metric_value": 0.9997, "depth": 3}
			if obj[1]>3:
				# {"feature": "Distance", "instances": 25, "metric_value": 0.971, "depth": 4}
				if obj[5]<=2:
					# {"feature": "Education", "instances": 23, "metric_value": 0.9877, "depth": 5}
					if obj[2]<=4:
						# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.976, "depth": 6}
						if obj[4]<=2.0:
							return 'False'
						elif obj[4]>2.0:
							return 'True'
						else: return 'True'
					elif obj[2]>4:
						return 'True'
					else: return 'True'
				elif obj[5]>2:
					return 'False'
				else: return 'False'
			elif obj[1]<=3:
				# {"feature": "Education", "instances": 22, "metric_value": 0.976, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 0.9928, "depth": 5}
					if obj[4]<=2.0:
						# {"feature": "Distance", "instances": 18, "metric_value": 0.9641, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					elif obj[4]>2.0:
						return 'False'
					else: return 'False'
				elif obj[2]>3:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[3]>20:
			return 'False'
		else: return 'False'
	elif obj[0]>1:
		# {"feature": "Distance", "instances": 34, "metric_value": 0.6024, "depth": 2}
		if obj[5]>1:
			# {"feature": "Occupation", "instances": 22, "metric_value": 0.7732, "depth": 3}
			if obj[3]>4:
				# {"feature": "Coupon", "instances": 16, "metric_value": 0.5436, "depth": 4}
				if obj[1]>1:
					return 'True'
				elif obj[1]<=1:
					# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[2]<=0:
						# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[4]>0.0:
							return 'True'
						elif obj[4]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[2]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[3]<=4:
				# {"feature": "Coupon", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[1]>2:
					# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[2]<=1:
						# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]<=0.0:
							return 'True'
						elif obj[4]>0.0:
							return 'True'
						else: return 'True'
					elif obj[2]>1:
						return 'False'
					else: return 'False'
				elif obj[1]<=2:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[5]<=1:
			return 'True'
		else: return 'True'
	else: return 'True'
