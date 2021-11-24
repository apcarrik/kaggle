def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Distance", "instances": 127, "metric_value": 0.9566, "depth": 1}
	if obj[5]<=1:
		# {"feature": "Occupation", "instances": 64, "metric_value": 0.8351, "depth": 2}
		if obj[3]<=14:
			# {"feature": "Passanger", "instances": 58, "metric_value": 0.7355, "depth": 3}
			if obj[0]>0:
				# {"feature": "Coupon", "instances": 50, "metric_value": 0.795, "depth": 4}
				if obj[1]>1:
					# {"feature": "Education", "instances": 38, "metric_value": 0.6892, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.4798, "depth": 6}
						if obj[4]<=1.0:
							return 'True'
						elif obj[4]>1.0:
							return 'True'
						else: return 'True'
					elif obj[2]>2:
						# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[4]<=1.0:
							return 'True'
						elif obj[4]>1.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[1]<=1:
					# {"feature": "Education", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 1.0, "depth": 6}
						if obj[4]<=2.0:
							return 'False'
						elif obj[4]>2.0:
							return 'True'
						else: return 'True'
					elif obj[2]>2:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		elif obj[3]>14:
			# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[0]<=1:
				return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[5]>1:
		# {"feature": "Education", "instances": 63, "metric_value": 0.9998, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Occupation", "instances": 57, "metric_value": 0.9944, "depth": 3}
			if obj[3]>0:
				# {"feature": "Restaurant20to50", "instances": 54, "metric_value": 0.999, "depth": 4}
				if obj[4]<=1.0:
					# {"feature": "Coupon", "instances": 38, "metric_value": 0.9678, "depth": 5}
					if obj[1]>0:
						# {"feature": "Passanger", "instances": 31, "metric_value": 0.9932, "depth": 6}
						if obj[0]<=2:
							return 'False'
						elif obj[0]>2:
							return 'False'
						else: return 'False'
					elif obj[1]<=0:
						# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[0]<=2:
							return 'False'
						elif obj[0]>2:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[4]>1.0:
					# {"feature": "Coupon", "instances": 16, "metric_value": 0.896, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Passanger", "instances": 10, "metric_value": 0.469, "depth": 6}
						if obj[0]>0:
							return 'True'
						elif obj[0]<=0:
							return 'False'
						else: return 'False'
					elif obj[1]>3:
						# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=1:
							return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[3]<=0:
				return 'False'
			else: return 'False'
		elif obj[2]>3:
			return 'True'
		else: return 'True'
	else: return 'True'
