def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Passanger", "instances": 85, "metric_value": 0.9143, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Occupation", "instances": 56, "metric_value": 0.9769, "depth": 2}
		if obj[3]<=21:
			# {"feature": "Education", "instances": 52, "metric_value": 0.9904, "depth": 3}
			if obj[2]<=4:
				# {"feature": "Distance", "instances": 49, "metric_value": 0.9973, "depth": 4}
				if obj[5]<=1:
					# {"feature": "Restaurant20to50", "instances": 26, "metric_value": 0.9612, "depth": 5}
					if obj[4]>-1.0:
						# {"feature": "Coupon", "instances": 25, "metric_value": 0.9427, "depth": 6}
						if obj[1]>2:
							return 'True'
						elif obj[1]<=2:
							return 'True'
						else: return 'True'
					elif obj[4]<=-1.0:
						return 'False'
					else: return 'False'
				elif obj[5]>1:
					# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9877, "depth": 5}
					if obj[4]<=2.0:
						# {"feature": "Coupon", "instances": 21, "metric_value": 0.9587, "depth": 6}
						if obj[1]>2:
							return 'False'
						elif obj[1]<=2:
							return 'False'
						else: return 'False'
					elif obj[4]>2.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[2]>4:
				return 'True'
			else: return 'True'
		elif obj[3]>21:
			return 'True'
		else: return 'True'
	elif obj[0]>1:
		# {"feature": "Coupon", "instances": 29, "metric_value": 0.6632, "depth": 2}
		if obj[1]>0:
			# {"feature": "Restaurant20to50", "instances": 26, "metric_value": 0.3912, "depth": 3}
			if obj[4]<=1.0:
				return 'True'
			elif obj[4]>1.0:
				# {"feature": "Occupation", "instances": 13, "metric_value": 0.6194, "depth": 4}
				if obj[3]<=12:
					# {"feature": "Education", "instances": 12, "metric_value": 0.4138, "depth": 5}
					if obj[2]>1:
						# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[5]<=2:
							return 'True'
						else: return 'True'
					elif obj[2]<=1:
						return 'True'
					else: return 'True'
				elif obj[3]>12:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[1]<=0:
			return 'False'
		else: return 'False'
	else: return 'True'
